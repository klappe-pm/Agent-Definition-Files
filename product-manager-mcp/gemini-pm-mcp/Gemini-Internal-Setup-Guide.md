---
categories: LLM  
subCategories:
  - deployment
  - gemini
  - infrastructure
topics:
  - Gemini Deployment
  - Internal Setup
  - Product Management
subTopics:
dateCreated: 2025-09-02  
dateRevised: 2025-09-02
aliases: [Gemini Infrastructure, Gemini Internal Setup]
tags: [deployment, gemini, infrastructure, internal-setup]
---

# Gemini Internal Setup Guide for PM MCP

## Executive Summary

This guide provides comprehensive instructions for setting up Gemini models internally for enterprise Product Manager MCP deployment. It covers infrastructure requirements, security configuration, integration setup, and operational procedures for running Gemini at scale.

## Infrastructure Architecture

### High-Level Architecture

```mermaid
flowchart TD
    subgraph External
        U[PM Users]
        W[Web Interface]
        C[CLI Tools]
    end
    
    subgraph LoadBalancer
        LB[Google Cloud Load Balancer]
        CDN[Cloud CDN]
    end
    
    subgraph ApplicationLayer
        API[API Gateway]
        AUTH[Authentication Service]
        ORCH[Gemini Orchestrator]
    end
    
    subgraph ModelLayer
        subgraph GeminiModels
            MF[Gemini Flash Cluster]
            MP[Gemini Pro Cluster]
            MV[Gemini Vision Cluster]
            MC[Gemini Code Cluster]
        end
    end
    
    subgraph DataLayer
        CACHE[Redis Cache]
        DB[Cloud SQL]
        STORE[Cloud Storage]
        BQ[BigQuery Analytics]
    end
    
    subgraph Monitoring
        LOG[Cloud Logging]
        MON[Cloud Monitoring]
        TRACE[Cloud Trace]
    end
    
    U --> W
    U --> C
    W --> LB
    C --> LB
    LB --> CDN
    CDN --> API
    API --> AUTH
    AUTH --> ORCH
    ORCH --> MF
    ORCH --> MP
    ORCH --> MV
    ORCH --> MC
    ORCH --> CACHE
    ORCH --> DB
    ORCH --> STORE
    ORCH --> BQ
    ORCH --> LOG
    ORCH --> MON
    ORCH --> TRACE
    
    style ORCH fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px
    style MF fill:#c8e6c9,stroke:#388e3c,stroke-width:2px
    style MP fill:#a5d6a7,stroke:#43a047,stroke-width:2px
```

## Google Cloud Platform Setup

### 1. Project Configuration

```bash
# Create new GCP project
gcloud projects create pm-mcp-production \
  --name="PM MCP Production" \
  --labels=environment=production,team=product

# Set project
gcloud config set project pm-mcp-production

# Enable required APIs
gcloud services enable \
  aiplatform.googleapis.com \
  compute.googleapis.com \
  container.googleapis.com \
  redis.googleapis.com \
  sqladmin.googleapis.com \
  storage.googleapis.com \
  bigquery.googleapis.com \
  cloudkms.googleapis.com \
  secretmanager.googleapis.com \
  monitoring.googleapis.com \
  logging.googleapis.com \
  cloudtrace.googleapis.com

# Set default region
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a
```

### 2. IAM and Security Setup

```bash
# Create service accounts
gcloud iam service-accounts create gemini-orchestrator \
  --display-name="Gemini Orchestrator Service"

gcloud iam service-accounts create gemini-api \
  --display-name="Gemini API Service"

gcloud iam service-accounts create gemini-monitoring \
  --display-name="Gemini Monitoring Service"

# Assign roles
gcloud projects add-iam-policy-binding pm-mcp-production \
  --member="serviceAccount:gemini-orchestrator@pm-mcp-production.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

gcloud projects add-iam-policy-binding pm-mcp-production \
  --member="serviceAccount:gemini-api@pm-mcp-production.iam.gserviceaccount.com" \
  --role="roles/aiplatform.viewer"

# Create custom roles
cat > gemini-pm-role.yaml << EOF
title: "Gemini PM User"
description: "Role for PM users accessing Gemini"
stage: "GA"
includedPermissions:
- aiplatform.models.predict
- aiplatform.endpoints.predict
- storage.objects.get
- storage.objects.list
- bigquery.datasets.get
- bigquery.tables.list
EOF

gcloud iam roles create geminiPMUser \
  --project=pm-mcp-production \
  --file=gemini-pm-role.yaml
```

### 3. Kubernetes Cluster Setup

```bash
# Create GKE cluster for Gemini orchestration
gcloud container clusters create gemini-pm-cluster \
  --region=us-central1 \
  --num-nodes=3 \
  --node-locations=us-central1-a,us-central1-b,us-central1-c \
  --machine-type=n2-standard-8 \
  --enable-autoscaling \
  --min-nodes=3 \
  --max-nodes=20 \
  --enable-autorepair \
  --enable-autoupgrade \
  --enable-ip-alias \
  --network=projects/pm-mcp-production/global/networks/default \
  --enable-stackdriver-kubernetes \
  --enable-cloud-monitoring \
  --workload-pool=pm-mcp-production.svc.id.goog

# Get cluster credentials
gcloud container clusters get-credentials gemini-pm-cluster --region=us-central1

# Install required components
kubectl create namespace gemini-pm
kubectl create namespace monitoring
kubectl create namespace redis
```

## Gemini Model Deployment

### 1. Model Endpoint Configuration

```python
# deploy_gemini_endpoints.py
from google.cloud import aiplatform
import json

def deploy_gemini_endpoints():
    """Deploy Gemini model endpoints"""
    
    aiplatform.init(
        project='pm-mcp-production',
        location='us-central1'
    )
    
    # Model configurations
    models = {
        'gemini-flash': {
            'model_name': 'gemini-2.0-flash',
            'machine_type': 'n1-standard-4',
            'min_replica_count': 2,
            'max_replica_count': 10,
            'accelerator_type': None,
            'accelerator_count': 0
        },
        'gemini-pro': {
            'model_name': 'gemini-2.0-pro',
            'machine_type': 'n1-standard-8',
            'min_replica_count': 2,
            'max_replica_count': 5,
            'accelerator_type': 'NVIDIA_TESLA_T4',
            'accelerator_count': 1
        },
        'gemini-vision': {
            'model_name': 'gemini-2.0-pro-vision',
            'machine_type': 'n1-standard-8',
            'min_replica_count': 1,
            'max_replica_count': 3,
            'accelerator_type': 'NVIDIA_TESLA_T4',
            'accelerator_count': 1
        },
        'gemini-code': {
            'model_name': 'gemini-2.0-pro-code',
            'machine_type': 'n1-standard-8',
            'min_replica_count': 1,
            'max_replica_count': 3,
            'accelerator_type': None,
            'accelerator_count': 0
        }
    }
    
    endpoints = {}
    
    for name, config in models.items():
        print(f"Deploying {name}...")
        
        # Create endpoint
        endpoint = aiplatform.Endpoint.create(
            display_name=f'gemini-pm-{name}',
            labels={'model': name, 'environment': 'production'}
        )
        
        # Deploy model
        model = aiplatform.Model(
            model_name=f"projects/pm-mcp-production/locations/us-central1/models/{config['model_name']}"
        )
        
        endpoint.deploy(
            model=model,
            deployed_model_display_name=name,
            machine_type=config['machine_type'],
            min_replica_count=config['min_replica_count'],
            max_replica_count=config['max_replica_count'],
            accelerator_type=config['accelerator_type'],
            accelerator_count=config['accelerator_count'],
            traffic_percentage=100
        )
        
        endpoints[name] = endpoint.resource_name
        print(f"Deployed {name} to {endpoint.resource_name}")
    
    # Save endpoint configuration
    with open('endpoints.json', 'w') as f:
        json.dump(endpoints, f, indent=2)
    
    return endpoints

if __name__ == "__main__":
    deploy_gemini_endpoints()
```

### 2. Orchestrator Service Deployment

```yaml
# gemini-orchestrator-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gemini-orchestrator
  namespace: gemini-pm
spec:
  replicas: 3
  selector:
    matchLabels:
      app: gemini-orchestrator
  template:
    metadata:
      labels:
        app: gemini-orchestrator
    spec:
      serviceAccountName: gemini-orchestrator
      containers:
      - name: orchestrator
        image: gcr.io/pm-mcp-production/gemini-orchestrator:latest
        ports:
        - containerPort: 8080
          name: http
        - containerPort: 9090
          name: metrics
        env:
        - name: PROJECT_ID
          value: pm-mcp-production
        - name: REGION
          value: us-central1
        - name: REDIS_HOST
          value: redis-service.redis.svc.cluster.local
        - name: DB_CONNECTION
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: connection-string
        resources:
          requests:
            memory: "2Gi"
            cpu: "1"
          limits:
            memory: "4Gi"
            cpu: "2"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: gemini-orchestrator-service
  namespace: gemini-pm
spec:
  selector:
    app: gemini-orchestrator
  ports:
  - name: http
    port: 80
    targetPort: 8080
  - name: metrics
    port: 9090
    targetPort: 9090
  type: LoadBalancer
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: gemini-orchestrator-hpa
  namespace: gemini-pm
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: gemini-orchestrator
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

## Security Configuration

### 1. Network Security

```yaml
# network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: gemini-network-policy
  namespace: gemini-pm
spec:
  podSelector:
    matchLabels:
      app: gemini-orchestrator
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: redis
    ports:
    - protocol: TCP
      port: 6379
  - to:
    - namespaceSelector:
        matchLabels:
          name: gemini-models
  - ports:
    - protocol: TCP
      port: 443  # HTTPS for external APIs
```

### 2. Secret Management

```bash
# Create secrets
echo -n "your-gemini-api-key" | gcloud secrets create gemini-api-key \
  --data-file=- \
  --replication-policy="automatic"

echo -n "postgresql://user:pass@host/db" | gcloud secrets create db-connection \
  --data-file=- \
  --replication-policy="automatic"

# Grant access to service account
gcloud secrets add-iam-policy-binding gemini-api-key \
  --member="serviceAccount:gemini-orchestrator@pm-mcp-production.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

### 3. Encryption Configuration

```python
# encryption_manager.py
from google.cloud import kms
import base64
from cryptography.fernet import Fernet

class EncryptionManager:
    """Manage encryption for sensitive data"""
    
    def __init__(self, project_id, location, key_ring, key_name):
        self.client = kms.KeyManagementServiceClient()
        self.key_path = self.client.crypto_key_path(
            project_id, location, key_ring, key_name
        )
        
    def encrypt_data(self, plaintext: str) -> str:
        """Encrypt data using Cloud KMS"""
        
        plaintext_bytes = plaintext.encode('utf-8')
        
        response = self.client.encrypt(
            request={
                'name': self.key_path,
                'plaintext': plaintext_bytes
            }
        )
        
        return base64.b64encode(response.ciphertext).decode('utf-8')
    
    def decrypt_data(self, ciphertext: str) -> str:
        """Decrypt data using Cloud KMS"""
        
        ciphertext_bytes = base64.b64decode(ciphertext)
        
        response = self.client.decrypt(
            request={
                'name': self.key_path,
                'ciphertext': ciphertext_bytes
            }
        )
        
        return response.plaintext.decode('utf-8')
```

## Monitoring and Observability

### 1. Metrics Collection

```yaml
# prometheus-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: monitoring
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
      evaluation_interval: 15s
    
    scrape_configs:
    - job_name: 'gemini-orchestrator'
      kubernetes_sd_configs:
      - role: pod
        namespaces:
          names:
          - gemini-pm
      relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        action: keep
        regex: gemini-orchestrator
    
    - job_name: 'gemini-models'
      static_configs:
      - targets:
        - 'gemini-flash-metrics:9090'
        - 'gemini-pro-metrics:9090'
        - 'gemini-vision-metrics:9090'
        - 'gemini-code-metrics:9090'
    
    rule_files:
    - /etc/prometheus/rules/*.yml
    
    alerting:
      alertmanagers:
      - static_configs:
        - targets:
          - alertmanager:9093
```

### 2. Alert Rules

```yaml
# alert-rules.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: alert-rules
  namespace: monitoring
data:
  gemini-alerts.yml: |
    groups:
    - name: gemini_alerts
      interval: 30s
      rules:
      - alert: HighErrorRate
        expr: rate(gemini_errors_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: High error rate detected
          description: "Error rate is {{ $value }} errors per second"
      
      - alert: HighLatency
        expr: histogram_quantile(0.95, gemini_request_duration_seconds) > 2
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: High latency detected
          description: "95th percentile latency is {{ $value }} seconds"
      
      - alert: LowCacheHitRate
        expr: rate(cache_hits[5m]) / rate(cache_requests[5m]) < 0.5
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: Low cache hit rate
          description: "Cache hit rate is {{ $value }}"
      
      - alert: HighTokenUsage
        expr: sum(rate(gemini_tokens_used[1h])) > 1000000
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: High token usage
          description: "Token usage is {{ $value }} per hour"
```

### 3. Logging Configuration

```python
# logging_config.py
import logging
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler
import json

def setup_logging():
    """Configure structured logging for Gemini PM MCP"""
    
    # Setup Google Cloud Logging
    client = google.cloud.logging.Client()
    handler = CloudLoggingHandler(client)
    
    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[handler]
    )
    
    # Create custom logger
    logger = logging.getLogger('gemini_pm_mcp')
    
    return logger

class StructuredLogger:
    """Structured logging for better observability"""
    
    def __init__(self, logger):
        self.logger = logger
    
    def log_request(self, task_id, task_type, model, user_id):
        """Log incoming request"""
        
        self.logger.info(json.dumps({
            'event': 'request_received',
            'task_id': task_id,
            'task_type': task_type,
            'model': model,
            'user_id': user_id,
            'timestamp': datetime.now().isoformat()
        }))
    
    def log_response(self, task_id, success, latency, tokens_used):
        """Log response"""
        
        self.logger.info(json.dumps({
            'event': 'response_sent',
            'task_id': task_id,
            'success': success,
            'latency_ms': latency,
            'tokens_used': tokens_used,
            'timestamp': datetime.now().isoformat()
        }))
    
    def log_error(self, task_id, error, traceback):
        """Log error"""
        
        self.logger.error(json.dumps({
            'event': 'error_occurred',
            'task_id': task_id,
            'error': str(error),
            'traceback': traceback,
            'timestamp': datetime.now().isoformat()
        }))
```

## Backup and Disaster Recovery

### 1. Backup Strategy

```bash
#!/bin/bash
# backup_strategy.sh

# Database backup
gcloud sql backups create \
  --instance=gemini-pm-db \
  --description="Daily backup $(date +%Y%m%d)"

# Export to Cloud Storage
gcloud sql export sql gemini-pm-db \
  gs://pm-mcp-backups/db/backup-$(date +%Y%m%d).sql \
  --database=gemini_pm_mcp

# Redis backup
kubectl exec -n redis redis-0 -- redis-cli BGSAVE
kubectl cp redis/redis-0:/data/dump.rdb \
  ./backups/redis-backup-$(date +%Y%m%d).rdb

# Upload to Cloud Storage
gsutil cp ./backups/redis-backup-$(date +%Y%m%d).rdb \
  gs://pm-mcp-backups/redis/

# Configuration backup
kubectl get all --all-namespaces -o yaml > k8s-backup-$(date +%Y%m%d).yaml
gsutil cp k8s-backup-$(date +%Y%m%d).yaml \
  gs://pm-mcp-backups/k8s/
```

### 2. Disaster Recovery Plan

```python
# disaster_recovery.py
import subprocess
import time
from datetime import datetime

class DisasterRecovery:
    """Disaster recovery procedures for Gemini PM MCP"""
    
    def __init__(self):
        self.backup_bucket = 'gs://pm-mcp-backups'
        self.project_id = 'pm-mcp-production'
    
    def initiate_recovery(self, recovery_point: str):
        """Initiate disaster recovery from specific point"""
        
        print(f"Starting disaster recovery from {recovery_point}")
        
        # Step 1: Restore database
        self.restore_database(recovery_point)
        
        # Step 2: Restore Redis
        self.restore_redis(recovery_point)
        
        # Step 3: Restore Kubernetes configs
        self.restore_k8s_configs(recovery_point)
        
        # Step 4: Verify endpoints
        self.verify_endpoints()
        
        # Step 5: Run health checks
        self.run_health_checks()
        
        print("Disaster recovery completed")
    
    def restore_database(self, recovery_point: str):
        """Restore database from backup"""
        
        backup_file = f"{self.backup_bucket}/db/backup-{recovery_point}.sql"
        
        # Create new instance if needed
        subprocess.run([
            'gcloud', 'sql', 'instances', 'create', 
            'gemini-pm-db-recovery',
            '--database-version=POSTGRES_14',
            '--tier=db-n1-standard-4',
            '--region=us-central1'
        ])
        
        # Import backup
        subprocess.run([
            'gcloud', 'sql', 'import', 'sql',
            'gemini-pm-db-recovery',
            backup_file,
            '--database=gemini_pm_mcp'
        ])
        
        print(f"Database restored from {backup_file}")
    
    def restore_redis(self, recovery_point: str):
        """Restore Redis from backup"""
        
        backup_file = f"redis-backup-{recovery_point}.rdb"
        
        # Download backup
        subprocess.run([
            'gsutil', 'cp',
            f"{self.backup_bucket}/redis/{backup_file}",
            f"./recovery/{backup_file}"
        ])
        
        # Copy to Redis pod
        subprocess.run([
            'kubectl', 'cp',
            f"./recovery/{backup_file}",
            'redis/redis-0:/data/dump.rdb'
        ])
        
        # Restart Redis
        subprocess.run([
            'kubectl', 'rollout', 'restart',
            'statefulset/redis', '-n', 'redis'
        ])
        
        print(f"Redis restored from {backup_file}")
```

## Performance Tuning

### 1. Model Optimization

```python
# performance_tuning.py
class ModelPerformanceTuner:
    """Optimize Gemini model performance"""
    
    def __init__(self):
        self.performance_metrics = {}
        
    def optimize_batch_size(self, model_name: str):
        """Find optimal batch size for model"""
        
        batch_sizes = [1, 2, 4, 8, 16, 32]
        results = {}
        
        for batch_size in batch_sizes:
            latency = self.test_batch_performance(model_name, batch_size)
            throughput = batch_size / latency
            results[batch_size] = {
                'latency': latency,
                'throughput': throughput
            }
        
        optimal = max(results.items(), key=lambda x: x[1]['throughput'])
        return optimal[0]
    
    def optimize_cache_strategy(self):
        """Optimize caching configuration"""
        
        cache_configs = [
            {'ttl': 300, 'max_size': '8GB'},
            {'ttl': 600, 'max_size': '16GB'},
            {'ttl': 1800, 'max_size': '32GB'},
            {'ttl': 3600, 'max_size': '64GB'}
        ]
        
        best_hit_rate = 0
        best_config = None
        
        for config in cache_configs:
            hit_rate = self.test_cache_performance(config)
            if hit_rate > best_hit_rate:
                best_hit_rate = hit_rate
                best_config = config
        
        return best_config
```

### 2. Resource Optimization

```yaml
# resource-optimization.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: optimization-config
  namespace: gemini-pm
data:
  config.yaml: |
    models:
      flash:
        batch_size: 16
        max_concurrent: 100
        timeout_ms: 5000
        cache_ttl: 1800
      pro:
        batch_size: 4
        max_concurrent: 20
        timeout_ms: 30000
        cache_ttl: 7200
      vision:
        batch_size: 2
        max_concurrent: 10
        timeout_ms: 60000
        cache_ttl: 3600
      code:
        batch_size: 4
        max_concurrent: 15
        timeout_ms: 45000
        cache_ttl: 10800
    
    resources:
      cpu_allocation:
        orchestrator: 2000m
        api_gateway: 1000m
        cache_proxy: 500m
      memory_allocation:
        orchestrator: 4Gi
        api_gateway: 2Gi
        cache_proxy: 1Gi
    
    autoscaling:
      metrics:
        - type: cpu
          target: 70
        - type: memory
          target: 80
        - type: custom/requests_per_second
          target: 1000
```

## Cost Management

### Monthly Cost Analysis

```python
# cost_analysis.py
class CostAnalyzer:
    """Analyze and optimize Gemini PM MCP costs"""
    
    def calculate_monthly_costs(self):
        """Calculate estimated monthly costs"""
        
        costs = {
            'compute': {
                'gke_cluster': 1500,  # 3-20 nodes
                'load_balancer': 25,
                'cloud_cdn': 50
            },
            'models': {
                'gemini_flash': 500,  # ~1M requests
                'gemini_pro': 2000,   # ~400K requests
                'gemini_vision': 300, # ~60K requests
                'gemini_code': 400    # ~80K requests
            },
            'storage': {
                'cloud_sql': 200,
                'redis': 150,
                'cloud_storage': 50,
                'bigquery': 100
            },
            'networking': {
                'egress': 100,
                'cloud_nat': 50
            },
            'monitoring': {
                'logging': 50,
                'monitoring': 25,
                'trace': 25
            }
        }
        
        total = sum(sum(v.values()) for v in costs.values())
        
        return {
            'breakdown': costs,
            'total_monthly': total,
            'per_user': total / 50  # Assuming 50 users
        }
    
    def optimization_recommendations(self):
        """Generate cost optimization recommendations"""
        
        return [
            "Use committed use discounts for compute resources",
            "Implement aggressive caching to reduce model calls",
            "Use Gemini Flash for simple tasks instead of Pro",
            "Archive old data to cold storage",
            "Use spot instances for non-critical workloads",
            "Implement request batching to reduce API calls"
        ]
```

## Maintenance Schedule

### Regular Maintenance Tasks

| Task | Frequency | Duration | Impact |
|------|-----------|----------|--------|
| Security patches | Weekly | 30 min | None |
| Database maintenance | Weekly | 1 hour | Minimal |
| Cache cleanup | Daily | 15 min | None |
| Log rotation | Daily | 5 min | None |
| Backup verification | Weekly | 30 min | None |
| Performance review | Monthly | 2 hours | None |
| Capacity planning | Quarterly | 4 hours | None |
| Disaster recovery test | Quarterly | 8 hours | Planned downtime |

## Conclusion

This comprehensive internal setup guide provides everything needed to deploy and operate a production-grade Gemini PM MCP system. The architecture leverages Google Cloud Platform's native integration with Gemini models, providing optimal performance, security, and scalability for enterprise product management automation.

Key benefits of this setup:

- **Native GCP integration** for optimal Gemini performance
- **Comprehensive security** with encryption, IAM, and network policies
- **High availability** with multi-zone deployment and auto-scaling
- **Cost optimization** through intelligent caching and model routing
- **Full observability** with monitoring, logging, and alerting
- **Disaster recovery** capabilities with automated backups

The system is designed to handle 50-100 concurrent PM users with sub-second response times for most operations while maintaining costs under $6,000/month.

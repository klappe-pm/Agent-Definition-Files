#!/usr/bin/env python3
"""
Convert JSON agent definitions to TOML and YAML formats
Maintains one-to-one mapping between JSON and output structures
"""

import json
import os
import sys
from pathlib import Path

# Optional dependencies
try:
    import toml  # type: ignore
except Exception:
    toml = None

try:
    import yaml  # PyYAML
except Exception:
    yaml = None


def clean_json_content(content: str) -> str:
    """Remove YAML frontmatter if present and clean JSON content"""
    if content.startswith('---'):
        lines = content.split('\n')
        yaml_end = -1
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                yaml_end = i
                break
        if yaml_end > 0:
            json_content = '\n'.join(lines[yaml_end + 1:])
            return json_content.strip()
    return content.strip()


def read_json_file(json_file_path: Path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    json_content = clean_json_content(content)
    return json.loads(json_content)


def write_toml(data, toml_file_path: Path):
    if toml is None:
        raise RuntimeError("toml library not available. Install with: python3 -m pip install --user toml")
    toml_content = toml.dumps(data)
    os.makedirs(os.path.dirname(toml_file_path), exist_ok=True)
    with open(toml_file_path, 'w', encoding='utf-8') as f:
        f.write(toml_content)


def write_yaml(data, yaml_file_path: Path):
    if yaml is None:
        raise RuntimeError("PyYAML not available. Install with: python3 -m pip install --user pyyaml")
    os.makedirs(os.path.dirname(yaml_file_path), exist_ok=True)
    with open(yaml_file_path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


def process_agent_directory(agent_dir: Path):
    json_dir = agent_dir / 'json'
    toml_dir = agent_dir / 'toml'
    yaml_dir = agent_dir / 'yaml'

    if not json_dir.exists():
        return {'converted_toml': 0, 'converted_yaml': 0}, []

    toml_dir.mkdir(exist_ok=True)
    yaml_dir.mkdir(exist_ok=True)

    stats = {'converted_toml': 0, 'converted_yaml': 0}
    errors = []

    json_files = list(json_dir.glob('*.json'))

    for json_file in json_files:
        try:
            data = read_json_file(json_file)
        except Exception as e:
            errors.append({'file': str(json_file), 'error': f'JSON parse error: {e}'})
            print(f"✗ Failed to parse: {json_file.name} - {e}")
            continue

        # TOML
        toml_file = toml_dir / (json_file.stem + '.toml')
        try:
            write_toml(data, toml_file)
            stats['converted_toml'] += 1
            print(f"✓ TOML: {json_file.name} -> {toml_file.name}")
        except Exception as e:
            errors.append({'file': str(json_file), 'error': f'TOML error: {e}'})
            print(f"✗ TOML failed: {json_file.name} - {e}")

        # YAML
        yaml_file = yaml_dir / (json_file.stem + '.yaml')
        try:
            write_yaml(data, yaml_file)
            stats['converted_yaml'] += 1
            print(f"✓ YAML: {json_file.name} -> {yaml_file.name}")
        except Exception as e:
            errors.append({'file': str(json_file), 'error': f'YAML error: {e}'})
            print(f"✗ YAML failed: {json_file.name} - {e}")

    return stats, errors


def main():
    agents_base_dir = Path('/Users/kevinlappe/Obsidian/Agents/agents')

    agent_directories = [
        'business-review-agent',
        'cloud agent',
        'content-agent',
        'context-agent',
        'engineering-agent',
        'google-apps-script-agent',
        'product-agents',
        'project-agent',
        'public-relations-agent',
        'research-agent',
        'ux-agent',
    ]

    total_toml = 0
    total_yaml = 0
    total_errors = []
    summary_report = []

    print("=" * 60)
    print("JSON to TOML & YAML Conversion Process")
    print("=" * 60)

    for agent_dir_name in agent_directories:
        agent_dir = agents_base_dir / agent_dir_name
        if not agent_dir.exists():
            print(f"\n⚠ Directory not found: {agent_dir_name}")
            continue

        print(f"\nProcessing: {agent_dir_name}")
        print("-" * 40)

        stats, errors = process_agent_directory(agent_dir)
        total_toml += stats['converted_toml']
        total_yaml += stats['converted_yaml']
        total_errors.extend(errors)

        summary_report.append({
            'directory': agent_dir_name,
            'toml': stats['converted_toml'],
            'yaml': stats['converted_yaml'],
            'errors': len(errors),
        })

    print("\n" + "=" * 60)
    print("CONVERSION SUMMARY")
    print("=" * 60)

    print(f"\nTotal agent categories processed: {len(agent_directories)}")
    print(f"Total TOML files converted: {total_toml}")
    print(f"Total YAML files converted: {total_yaml}")
    print(f"Total errors encountered: {len(total_errors)}")

    print("\n" + "-" * 40)
    print("Breakdown by Agent Category:")
    print("-" * 40)

    for item in summary_report:
        status = "✓" if item['errors'] == 0 else "⚠"
        print(f"{status} {item['directory']}: TOML {item['toml']}, YAML {item['yaml']}, Errors {item['errors']}")

    if total_errors:
        print("\n" + "-" * 40)
        print("ERRORS:")
        print("-" * 40)
        for error_info in total_errors:
            print(f"File: {error_info['file']}")
            print(f"  Error: {error_info['error']}")

    # Create summary report file
    summary_file = agents_base_dir / 'config_conversion_summary.txt'
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("JSON to TOML & YAML Conversion Summary\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total agent categories: {len(agent_directories)}\n")
        f.write(f"Total TOML files converted: {total_toml}\n")
        f.write(f"Total YAML files converted: {total_yaml}\n")
        f.write(f"Total errors: {len(total_errors)}\n\n")
        f.write("Breakdown by Agent Category:\n")
        f.write("-" * 40 + "\n")
        for item in summary_report:
            f.write(f"{item['directory']}: TOML {item['toml']}, YAML {item['yaml']}, Errors {item['errors']}\n")
        if total_errors:
            f.write("\nErrors:\n")
            f.write("-" * 40 + "\n")
            for error_info in total_errors:
                f.write(f"{error_info['file']}: {error_info['error']}\n")

    print(f"\n✓ Summary report saved to: {summary_file}")

    return 0 if len(total_errors) == 0 else 1


if __name__ == '__main__':
    sys.exit(main())

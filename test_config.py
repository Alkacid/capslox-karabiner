#!/usr/bin/env python3
"""
Simple test script to validate the configuration transformation.
"""

import json
import sys


def validate_config(config_file, expected_key):
    """Validate that a configuration file uses the expected key."""
    
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    errors = []
    
    # Check 1: Capslock should map to the expected key
    capslock_manip = config['rules'][0]['manipulators'][0]
    if capslock_manip['from']['key_code'] != 'caps_lock':
        errors.append("First manipulator is not for caps_lock")
    
    capslock_to = capslock_manip['to'][0]['key_code']
    if capslock_to != expected_key:
        errors.append(f"Capslock maps to {capslock_to}, expected {expected_key}")
    
    # Check 2: No Hyper modifier combos should remain in mandatory modifiers
    hyper_set = {'right_command', 'right_control', 'right_option', 'right_shift'}
    for rule in config['rules']:
        for manip in rule['manipulators']:
            if 'from' in manip and 'modifiers' in manip['from']:
                if 'mandatory' in manip['from']['modifiers']:
                    mods = set(manip['from']['modifiers']['mandatory'])
                    if hyper_set.issubset(mods):
                        errors.append(f"Found Hyper combo in mandatory modifiers")
                        break
    
    # Check 3: Expected key should appear in modifiers
    key_count = 0
    for rule in config['rules']:
        for manip in rule['manipulators']:
            if 'from' in manip and 'modifiers' in manip['from']:
                if 'mandatory' in manip['from']['modifiers']:
                    if expected_key in manip['from']['modifiers']['mandatory']:
                        key_count += 1
    
    if key_count == 0:
        errors.append(f"Expected key {expected_key} not found in any modifiers")
    
    # Check 4: Title should mention the key
    if 'title' in config:
        if expected_key.upper() not in config['title']:
            errors.append(f"Title does not mention {expected_key.upper()}: {config['title']}")
    
    return errors


def main():
    print("🧪 Testing generated configurations...\n")
    
    # Test F19 version
    print("Testing capslox-karabiner-f19.json...")
    errors = validate_config('capslox-karabiner-f19.json', 'f19')
    if errors:
        print("  ❌ Errors found:")
        for error in errors:
            print(f"     - {error}")
        return 1
    else:
        print("  ✅ All checks passed!\n")
    
    # Test F20 version
    print("Testing capslox-karabiner-f20.json...")
    errors = validate_config('capslox-karabiner-f20.json', 'f20')
    if errors:
        print("  ❌ Errors found:")
        for error in errors:
            print(f"     - {error}")
        return 1
    else:
        print("  ✅ All checks passed!\n")
    
    # Summary statistics
    with open('capslox-karabiner-f19.json', 'r') as f:
        f19_config = json.load(f)
    
    total_rules = len(f19_config['rules'])
    total_manipulators = sum(len(rule['manipulators']) for rule in f19_config['rules'])
    
    print("📊 Configuration Statistics:")
    print(f"   Total rules: {total_rules}")
    print(f"   Total manipulators: {total_manipulators}")
    print(f"   Version: {f19_config['version']}")
    
    print("\n✅ All tests passed!")
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("   Make sure to run generate_f19_config.py first")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

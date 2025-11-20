#!/usr/bin/env python3
"""
Compare original and F19/F20 configurations to show the differences.
"""

import json
import sys


def analyze_modifiers(config):
    """Analyze modifier usage in a configuration."""
    stats = {
        'hyper_combo': 0,
        'f19': 0,
        'f20': 0,
        'total_manipulators': 0
    }
    
    hyper_set = {'right_command', 'right_control', 'right_option', 'right_shift'}
    
    for rule in config['rules']:
        for manip in rule['manipulators']:
            stats['total_manipulators'] += 1
            
            # Check 'from' modifiers
            if 'from' in manip and 'modifiers' in manip['from']:
                if 'mandatory' in manip['from']['modifiers']:
                    mods = set(manip['from']['modifiers']['mandatory'])
                    if hyper_set.issubset(mods):
                        stats['hyper_combo'] += 1
                    if 'f19' in mods:
                        stats['f19'] += 1
                    if 'f20' in mods:
                        stats['f20'] += 1
            
            # Check 'to' for Hyper mapping
            if 'to' in manip:
                for to_item in manip['to']:
                    if to_item.get('key_code') == 'right_shift':
                        if 'modifiers' in to_item:
                            mods = set(to_item.get('modifiers', []))
                            expected = {'right_command', 'right_control', 'right_option'}
                            if expected.issubset(mods):
                                stats['hyper_combo'] += 1
    
    return stats


def main():
    print("📊 Comparing Configurations\n")
    print("=" * 70)
    
    # Load and analyze original
    try:
        with open('capslox-karabiner-modified.json', 'r') as f:
            original = json.load(f)
        print("\n🔵 Original Configuration (Hyper with modifier combo)")
        print("   File: capslox-karabiner-modified.json")
        print(f"   Title: {original.get('title', 'N/A')}")
        print(f"   Version: {original.get('version', 'N/A')}")
        
        orig_stats = analyze_modifiers(original)
        print(f"   Total manipulators: {orig_stats['total_manipulators']}")
        print(f"   Uses Hyper combo: {orig_stats['hyper_combo']} occurrences")
        print(f"   Capslock maps to: right_shift + modifiers")
    except FileNotFoundError:
        print("\n⚠️  Original file not found: capslox-karabiner-modified.json")
        orig_stats = None
    
    # Load and analyze F19
    try:
        with open('capslox-karabiner-f19.json', 'r') as f:
            f19 = json.load(f)
        print("\n🟢 F19 Edition")
        print("   File: capslox-karabiner-f19.json")
        print(f"   Title: {f19.get('title', 'N/A')}")
        print(f"   Version: {f19.get('version', 'N/A')}")
        
        f19_stats = analyze_modifiers(f19)
        print(f"   Total manipulators: {f19_stats['total_manipulators']}")
        print(f"   Uses F19: {f19_stats['f19']} occurrences")
        print(f"   Uses Hyper combo: {f19_stats['hyper_combo']} occurrences")
        print(f"   Capslock maps to: f19")
    except FileNotFoundError:
        print("\n⚠️  F19 file not found. Run: python3 generate_f19_config.py")
        f19_stats = None
    
    # Load and analyze F20
    try:
        with open('capslox-karabiner-f20.json', 'r') as f:
            f20 = json.load(f)
        print("\n🟣 F20 Edition")
        print("   File: capslox-karabiner-f20.json")
        print(f"   Title: {f20.get('title', 'N/A')}")
        print(f"   Version: {f20.get('version', 'N/A')}")
        
        f20_stats = analyze_modifiers(f20)
        print(f"   Total manipulators: {f20_stats['total_manipulators']}")
        print(f"   Uses F20: {f20_stats['f20']} occurrences")
        print(f"   Uses Hyper combo: {f20_stats['hyper_combo']} occurrences")
        print(f"   Capslock maps to: f20")
    except FileNotFoundError:
        print("\n⚠️  F20 file not found. Run: python3 generate_f19_config.py --key f20")
        f20_stats = None
    
    # Summary
    print("\n" + "=" * 70)
    print("\n💡 Key Differences:\n")
    print("   Original: Capslock → right_shift + right_command + right_control + right_option")
    print("   F19:      Capslock → f19 (single key, less conflicts)")
    print("   F20:      Capslock → f20 (single key, less conflicts)")
    print("\n   Advantages of F19/F20:")
    print("   • Less likely to conflict with app shortcuts")
    print("   • More stable behavior across applications")
    print("   • Easier to debug issues")
    print("   • Better compatibility")
    
    print("\n" + "=" * 70)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

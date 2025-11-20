#!/usr/bin/env python3
"""
Script to convert capslox-karabiner configuration from using modifier key combinations
to using F19/F20 key as the Hyper key.

This replaces the simultaneous pressing of right_command, right_control, right_option,
and right_shift with F19 or F20, which are less likely to cause conflicts in applications.

Usage:
    python3 generate_f19_config.py [input_file] [output_file] [--key F19|F20]
"""

import json
import sys
import argparse
from typing import Dict, List, Any


def is_hyper_modifier_combo(modifiers: List[str]) -> bool:
    """
    Check if a modifier list contains the Hyper key combination.
    Hyper = right_command + right_control + right_option + right_shift
    """
    hyper_set = {"right_command", "right_control", "right_option", "right_shift"}
    return hyper_set.issubset(set(modifiers))


def is_hyper_to_mapping(to_item: Dict[str, Any]) -> bool:
    """
    Check if a 'to' item represents the Hyper key mapping.
    This can be either:
    - key_code: right_shift with modifiers: [right_command, right_control, right_option]
    - or any other combination that represents all 4 right modifiers
    """
    if "key_code" not in to_item:
        return False
    
    key_code = to_item.get("key_code")
    modifiers = to_item.get("modifiers", [])
    
    # Check if this is the specific Hyper mapping pattern
    # right_shift as key + the other three as modifiers
    if key_code == "right_shift":
        expected_mods = {"right_command", "right_control", "right_option"}
        return expected_mods.issubset(set(modifiers))
    
    return False


def replace_hyper_in_modifiers(modifiers: List[str], hyper_key: str = "f19") -> List[str]:
    """
    Replace the Hyper modifier combination with F19/F20 in a modifier list.
    Keeps any additional modifiers that aren't part of Hyper.
    """
    hyper_set = {"right_command", "right_control", "right_option", "right_shift"}
    # Remove hyper modifiers and add the chosen function key
    new_modifiers = [m for m in modifiers if m not in hyper_set]
    new_modifiers.append(hyper_key)
    return new_modifiers


def transform_manipulator(manipulator: Dict[str, Any], hyper_key: str = "f19") -> Dict[str, Any]:
    """
    Transform a single manipulator to use F19/F20 instead of Hyper modifier combo.
    """
    # Deep copy to avoid modifying original
    new_manipulator = json.loads(json.dumps(manipulator))
    
    # Transform the "from" section
    if "from" in new_manipulator:
        from_section = new_manipulator["from"]
        if "modifiers" in from_section and "mandatory" in from_section["modifiers"]:
            mandatory = from_section["modifiers"]["mandatory"]
            if is_hyper_modifier_combo(mandatory):
                new_mandatory = replace_hyper_in_modifiers(mandatory, hyper_key)
                from_section["modifiers"]["mandatory"] = new_mandatory
    
    # Transform the "to" section - this is where Capslock is mapped to Hyper
    if "to" in new_manipulator:
        for i, to_item in enumerate(new_manipulator["to"]):
            # Check if this is mapping to the Hyper combo
            if is_hyper_to_mapping(to_item):
                # Replace with the chosen function key
                new_manipulator["to"][i] = {"key_code": hyper_key}
    
    return new_manipulator


def transform_config(input_file: str, output_file: str, hyper_key: str = "f19") -> None:
    """
    Transform the entire Karabiner configuration file.
    """
    # Read the input JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Validate the configuration structure
    if "rules" not in config:
        raise ValueError("Invalid Karabiner configuration: missing 'rules' key")
    
    # Update version and metadata
    config["version"] = "2.0.0"
    if "title" in config:
        config["title"] = config["title"] + f" ({hyper_key.upper()} Edition)"
    
    # Transform all manipulators in all rules
    transformation_count = 0
    if "rules" in config:
        for rule in config["rules"]:
            if "manipulators" in rule:
                new_manipulators = []
                for manipulator in rule["manipulators"]:
                    new_manip = transform_manipulator(manipulator, hyper_key)
                    new_manipulators.append(new_manip)
                    # Count if transformation occurred
                    if new_manip != manipulator:
                        transformation_count += 1
                rule["manipulators"] = new_manipulators
    
    # Write the output JSON file with proper formatting
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Successfully generated {output_file}")
    print(f"   - Replaced Hyper modifier combo with {hyper_key.upper()} key")
    print(f"   - Updated version to {config['version']}")
    print(f"   - Transformed {transformation_count} manipulators")


def main():
    parser = argparse.ArgumentParser(
        description="Convert capslox-karabiner config to use F19/F20 instead of Hyper modifier combo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s my-config.json my-config-f19.json
  %(prog)s --key f20
  %(prog)s input.json output.json --key f20
        """
    )
    parser.add_argument(
        'input_file',
        nargs='?',
        default='capslox-karabiner-modified.json',
        help='Input Karabiner configuration file (default: capslox-karabiner-modified.json)'
    )
    parser.add_argument(
        'output_file',
        nargs='?',
        default=None,
        help='Output configuration file (default: capslox-karabiner-{key}.json)'
    )
    parser.add_argument(
        '--key',
        choices=['f19', 'f20', 'F19', 'F20'],
        default='f19',
        help='Function key to use as Hyper replacement (default: f19)'
    )
    
    args = parser.parse_args()
    
    # Normalize key to lowercase
    hyper_key = args.key.lower()
    
    # Set default output file if not specified
    if args.output_file is None:
        args.output_file = f'capslox-karabiner-{hyper_key}.json'
    
    print(f"🔄 Transforming configuration...")
    print(f"   Input:  {args.input_file}")
    print(f"   Output: {args.output_file}")
    print(f"   Key:    {hyper_key.upper()}")
    print()
    
    try:
        transform_config(args.input_file, args.output_file, hyper_key)
        print()
        print("📝 Next steps:")
        print("   1. Review the generated file")
        print("   2. Copy to Karabiner-Elements config directory:")
        print(f"      cp {args.output_file} ~/.config/karabiner/assets/complex_modifications/")
        print("   3. Enable the rules in Karabiner-Elements preferences")
        print()
        print("   Or import via URL if hosted online:")
        print(f"      karabiner://karabiner/assets/complex_modifications/import?url=file://$(pwd)/{args.output_file}")
    except FileNotFoundError:
        print(f"❌ Error: Could not find input file '{args.input_file}'")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in input file: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

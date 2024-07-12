import sys

# Define eligibility criteria
MINIMUM_AGE = 18
REQUIRED_CRITERIA = ["has_passed_test", "is_citizen"]

def show_help():
    print("License Eligibility Checker")
    print("===========================")
    print("Commands:")
    print("  check <age> <criteria>  Check license eligibility")
    print("  help                    Show this help message")
    print("Example:")
    print("  python license_eligibility.py check 20 has_passed_test is_citizen")

def check_eligibility(age, criteria):
    if age < MINIMUM_AGE:
        print("Ineligible: Age must be at least 18.")
        return

    missing_criteria = [criterion for criterion in REQUIRED_CRITERIA if criterion not in criteria]
    if missing_criteria:
        print(f"Ineligible: Missing criteria - {', '.join(missing_criteria)}")
    else:
        print("Eligible for license.")

def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1]
    
    if command == "help":
        show_help()
    elif command == "check" and len(sys.argv) > 2:
        try:
            age = int(sys.argv[2])
            criteria = sys.argv[3:]
            check_eligibility(age, criteria)
        except ValueError:
            print("Error: Age must be a valid number.")
            show_help()
    else:
        print("Unknown command.")
        show_help()

if __name__ == "__main__":
    main()

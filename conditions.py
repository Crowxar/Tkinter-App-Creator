base_template = """# This is a generated script

def main():
    print("Starting script...")

    # Conditional block 1 start
    {conditional_code_1}
    # Conditional block 1 end

    # Conditional block 2 start
    {conditional_code_2}
    # Conditional block 2 end

    print("Script ended.")

if __name__ == "__main__":
    main()
"""

conditional_code_block_1 = """
    print("Condition 1 is true")
    for i in range(3):
        print(f"Loop iteration {i}")
"""

conditional_code_block_2 = """
    print("Condition 2 is true")
    print("Executing additional logic for condition 2")
"""

default_code_block = """
    print("No specific conditions met")
"""
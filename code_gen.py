def generate_code(function_name: str, arguments: dict = None) -> str:
    imports = "from functions import " + function_name + "\n"
    code = f"def main():\n    try:\n        "
    if arguments:
        arg_str = ", ".join([f"{k}='{v}'" if isinstance(v,str) else f"{k}={v}" for k, v in arguments.items()])
        code += f"result = {function_name}({arg_str})\n"
    else:
        code += f"result = {function_name}()\n"
    code += "        print(f'{function_name} executed successfully. Result: {{result}}')\n    except Exception as e:\n        print(f'Error executing function: {e}')\n\nif __name__ == \"__main__\":\n    main()"
    return imports + code
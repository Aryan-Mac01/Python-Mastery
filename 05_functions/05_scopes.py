def serve_chai():
    chai_type = "Masala"#local_scope
    print(f"Inside function {chai_type}")

chai_type = "Lemon" #global scope
serve_chai()

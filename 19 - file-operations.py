# 🎯 Quick Start: File Operations Demo
# Create and write to a file
with open("hello.txt", "w") as file:
    file.write("Hello, Python Files!")
    file.write("\nFile operations are awesome!")

# Read the file back
with open("hello.txt", "r") as file:
    content = file.read()
    print("📄 File content:")
    print(content)

# Check if file exists
import os
print(f"✅ File exists: {os.path.exists('hello.txt')}")

# Simple file workflow
print("\n🔄 File Workflow Demo:")
data = ["Learn Python", "Practice coding", "Build projects"]

# Write list to file
with open("goals.txt", "w") as file:
    for item in data:
        file.write(f"• {item}\n")

# Read and display
with open("goals.txt", "r") as file:
    print("📋 My Goals:")
    print(file.read())
# Clean up created files
os.remove("hello.txt")
os.remove("goals.txt")
print("🧹 Cleaned up created files.")


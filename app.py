import requests
import pysftp

def build_step():
    print("::group::Running build step")
    try:
        with open("demo_build_output.txt", "w") as f:
            f.write("This is a demo build output.\nBuild successful!")
    except Exception as e:
        print(f"Build step failed: {e}")
        exit(1)
    finally:
        print("::endgroup::")

def main():
    build_step()
    print("App Deployed.")

if __name__ == "__main__":
    main()

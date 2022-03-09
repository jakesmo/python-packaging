import argparse
import pkg_resources
from package import ClassA
from dotenv import load_dotenv
import os

if __name__ == "__main__":

    load_dotenv(".env")

    parser = argparse.ArgumentParser(
        f"PACKAGE {pkg_resources.get_distribution(os.getenv('PACKAGE_NAME')).version} - \
        A sample application."
    )
    parser.add_argument(
        "--happy",
        action="store_true",
        help="Turn that frown upside down.",
    )

    args = parser.parse_args()

    classA = ClassA(args.happy)
    classA.run()

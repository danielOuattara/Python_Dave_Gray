import argparse


def cla_parser():
    parser = argparse.ArgumentParser(description="Provide a personalized game experience.")
    parser.add_argument(
        "-n", "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game"
    )
    args = parser.parse_args()

    return args.name

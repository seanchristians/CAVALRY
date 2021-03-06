import argparse, os, cavalry


def main():

    path = os.path.dirname(__file__) + "/.secrets.json"

    parser = argparse.ArgumentParser(
        prog="cav",
        description="Utility to load environment variables. To persist the variables into your scope, run 'source cav {load,clear} [options]' or '. cav {load,clear} [options]'"
    )
    parser.add_argument(
        "-s",
        "--secrets",
        metavar="FILE",
        default=path,
        help="specify an alternate secrets file",
    )  # SECRETS should be set to wherever .secrets.json is located.

    subparsers = parser.add_subparsers(dest="action")
    store = subparsers.add_parser("store", help="store variables")
    delete = subparsers.add_parser("delete", help="delete variables")
    load = subparsers.add_parser("load", help="load variables")
    list = subparsers.add_parser("list", help="list stored data")
    clear = subparsers.add_parser("clear", help="clear variables from environment")

    store.add_argument("project", help="project to load")
    store.add_argument(
        "-k",
        "--key",
        metavar=("KEY", "VALUE"),
        nargs=2,
        default=[None] * 2,
        help="variable name and corresponding data",
    )
    store.add_argument(
        "-d",
        "--directory",
        nargs="?",
        const=os.getcwd(),
        type=os.path.abspath,
        help="tie project to a specific directory. Specifying without a value will default to the current working directory",
    )
    delete.add_argument("project", help="project to load")
    delete.add_argument("key", nargs="*", help="delete specific variables")

    load.add_argument("project", nargs="?", help="project to load")
    load.add_argument("var", nargs="*", help="load specific variables")
    clear.add_argument("project", help="project to load")
    clear.add_argument("var", nargs="*", help="clear specific variables")

    list.add_argument("project", nargs="*", help="project to load")

    args = parser.parse_args()

    secrets = cavalry.Secrets(args.secrets, create=True)

    if args.action == "store":
        secrets.store(
            args.project, key=args.key[0], value=args.key[1], directory=args.directory
        )
    elif args.action == "delete":
        secrets.delete(args.project, *args.key)
    elif args.action == "load":
        vars = secrets.load(args.project, *args.var)
        comp = [f"{k}={v}" for k, v in vars.items()]
        print(f"export {' '.join(comp)}")
    elif args.action == "list":
        data = secrets.list(*args.project)
        print(*data, sep="\n")
    elif args.action == "clear":
        vars = secrets.load(args.project, *args.var)
        comp = [f"{k}=" for k in vars.keys()]
        print(f"export {' '.join(comp)}")

    secrets.commit()


if __name__ == "__main__":
    main()

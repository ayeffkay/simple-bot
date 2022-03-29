from argparse import ArgumentParser
import dialog_utils
import random
random.seed(42)

parser = ArgumentParser()
parser.add_argument('--plots_folder', type=str)
parser.add_argument('--start_label', nargs='+', type=str)
parser.add_argument('--fallback_label', nargs='+', type=str)
parser.add_argument('--dialog_test_file', type=str, nargs='?')
parser.add_argument('--run_interactive', action='store_true')

args = parser.parse_args()
args.start_label = tuple(args.start_label)
args.fallback_label = tuple(args.fallback_label)
actor = dialog_utils.init_actor(args.plots_folder, args.start_label, args.fallback_label)

if args.dialog_test_file:
    dialog_utils.run_test(args.dialog_test_file, actor)
if args.run_interactive:
    dialog_utils.run_interactive_mode(actor)

import argparse
import os

from pyHIPIFY import hipify_python, is_hip_clang

parser = argparse.ArgumentParser(description='Top-level script for HIPifying, filling in most common parameters')
parser.add_argument(
    '--out-of-place-only',
    action='store_true',
    help='Whether to only run hipify out-of-place on source files')

parser.add_argument(
    '--project-directory',
    type=str,
    default='',
    help='The root of the project.',
    required=False)

parser.add_argument(
    '--output-directory',
    type=str,
    default='',
    help='The Directory to Store the Hipified Project',
    required=False)

parser.add_argument(
    '--include',
    type=str,
    default=[],
    nargs='+',
    help="The list of directories in caffe2 to hipify",
    required=False)

parser.add_argument(
    '--ignores',
    type=str,
    default=[],
    nargs='+',
    help="The list of directories to ignore",
    required=False)

args = parser.parse_args()

amd_build_dir = os.path.dirname(os.path.realpath(__file__))
proj_dir = os.path.join(os.path.dirname(os.path.dirname(amd_build_dir)))

if args.project_directory:
    proj_dir = args.project_directory

out_dir = proj_dir
if args.output_directory:
    out_dir = args.output_directory

# json_settings = os.path.join(amd_build_dir, 'disabled_features.json')

if not args.out_of_place_only:
    # Apply patch files in place (PyTorch only)
    patch_folder = os.path.join(amd_build_dir, 'patches')


includes = []

for new_dir in args.include:
    abs_new_dir = os.path.join(proj_dir, new_dir)
    if os.path.exists(abs_new_dir):
        new_dir = os.path.join(new_dir, '**/*')
        includes.append(new_dir)

hipify_python.hipify(
    project_directory=proj_dir,
    output_directory=out_dir,
    includes=includes,
    ignores=args.ignores,
    out_of_place_only=args.out_of_place_only,
    hip_clang_launch=is_hip_clang())

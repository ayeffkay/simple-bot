#!/bin/bash

python dialog_runner.py \
        --plots_folder dialog_plots \
        --start_label global_flow start_node \
        --fallback_label global_flow node_goodbye \
        --dialog_test_file tests/test3.in

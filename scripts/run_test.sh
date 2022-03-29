#!/bin/bash

python dialog_runner.py \
        --plots_folder dialog_plots \
        --start_label greeting_flow start_node \
        --fallback_label greeting_flow node_goodbye \
        --dialog_test_file tests/test2.in

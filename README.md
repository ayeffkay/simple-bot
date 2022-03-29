This is test bot. 

Structure:

    - `dialog_plots` - json files with plots
    - `scripts` - bash scripts to run (`test` and `interactive` modes available)
    - `tests` - test files
    - `dialog_runner.py` - command line util to start dialog into `test` or `interactive` modes
    - `dialog_utils.py` - building plots from json files, dialog handler, etc.
    - `transitions.py`, `responses.py` - condition and response functions

Launch bot using bash:

```
    bash scripts/run_test.sh
    bash scripts/run_interactive.sh
```

To run command line util explicitly:

```
    python dialog_runner.py --plots_folder dialog_plots \
                            --start_label greeting_flow start_node \
                            --fallback_label greeting_flow node_goodbye \
                            --dialog_test_file tests/test1.in
```

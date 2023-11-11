import argparse
import os

def get_args(database_name, BASE_DATA_DIR = "./data/"):
    
    parser = argparse.ArgumentParser(
        "LLM explorer.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--overwrite_cache",
        type=bool,
        default=0,
        help="Whether to overwrite the caching for prompts."
    )

    parser.add_argument(
        "--data_lake",
        type=str,
        default="fda_510ks",
        help="Name of the data lake"
    )

    parser.add_argument(
        "--data_dir",
        type=str,
        help="Path to raw data-lake documents",
    )

    parser.add_argument(
        "--generative_index_path",
        type=str,
        help="Path to store the generated structured view of the data lake",
    )

    parser.add_argument(
        "--cache_dir",
        type=str,
        default=".cache/",
        help="Path to cache intermediate files during system execution",
    )

    parser.add_argument(
        "--set_dicts",
        type=str,
        default='',
        help="Alternate valid names for the SWDE attributes as provided in the benchmark.",
    )

    parser.add_argument(
        "--topic",
        type=list,
        default=[],
        help="Topic of the data lake",
    )

    CONSTANTS = {
        "fda_510ks": {
            "data_dir": os.path.join(BASE_DATA_DIR, "fda_510ks/"),
            "database_name": "fda_510ks",
            "cache_dir": ".cache/fda_510ks/",
            "generative_index_path": os.path.join(BASE_DATA_DIR, "generative_indexes/fda_510ks/"),
            "gold_extractions_file": os.path.join(BASE_DATA_DIR, "ground_truth/fda_510ks_gold_extractions.json"),
            "topic": "fda 510k device premarket notifications",
        },
        "10k_corp": {
            "data_dir": os.path.join(BASE_DATA_DIR, "10k_corp/"),
            "database_name": "10k_corp",
            "cache_dir": ".cache/10k_corp/",
            "generative_index_path": os.path.join(BASE_DATA_DIR, "generative_indexes/10k_corp/"),
            "gold_extractions_file": os.path.join(BASE_DATA_DIR, "ground_truth/10k_corp_gold_extractions.json"),
            "topic": "10k Corporation financial documents",
        },
        "pdf_v1": {
            "data_dir": os.path.join(BASE_DATA_DIR, "pdf_v1/"),
            "database_name": "fda_510ks",
            "cache_dir": ".cache/pdf/",
            "generative_index_path": os.path.join(BASE_DATA_DIR, "generative_indexes/pdf/"),
            "gold_extractions_file": os.path.join(BASE_DATA_DIR, "ground_truth/pdf_gold_extractions.json"),
            "topic": "fda 510k device premarket notifications",
        }
    }

    args = parser.parse_args(args=[])
    args_fill = CONSTANTS[database_name]
    args.data_dir = args_fill["data_dir"]
    args.cache_dir = args_fill["cache_dir"]
    args.generative_index_path = args_fill["generative_index_path"]
    args.topic = args_fill['topic']
    args.gold_extractions_file = args_fill['gold_extractions_file']
    args.data_lake = database_name
    if 'set_dicts' in args_fill:
        args.set_dicts = args_fill['set_dicts']

    return args

#!/usr/bin/env python3
"""Parse GAIA evaluation results and format for leaderboard."""

import json
import sys
from datetime import datetime
from pathlib import Path


def parse_results(raw_results_path: str, output_path: str, agent_image: str, level: int, task_ids: str):
    """Parse raw evaluation results and create leaderboard JSON.

    Args:
        raw_results_path: Path to raw results JSON from client_cli
        output_path: Path to output leaderboard JSON
        agent_image: Docker image of the agent being evaluated
        level: GAIA difficulty level
        task_ids: Comma-separated task IDs
    """

    # Generate agent name and timestamp
    agent_name = agent_image.replace('/', '_').replace(':', '_')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Default result structure
    result = {
        "agent_id": agent_image,
        "agent_name": agent_name,
        "timestamp": timestamp,
        "level": level,
        "task_ids": task_ids,
        "accuracy": 0.0,
        "score": 0,
        "total": len(task_ids.split(',')),
        "avg_time": 0.0,
        "status": "failed",
        "note": "Evaluation failed to complete"
    }

    try:
        # Read raw results
        with open(raw_results_path, 'r') as f:
            raw_data = json.load(f)

        # Extract results from artifacts
        # The client_cli saves artifacts in the "results" field
        if "results" in raw_data and len(raw_data["results"]) > 0:
            eval_result = raw_data["results"][0]  # First artifact should have the evaluation data

            # Extract metrics
            if "accuracy" in eval_result:
                result["accuracy"] = round(eval_result["accuracy"], 2)
            if "score" in eval_result:
                result["score"] = eval_result["score"]
            if "max_score" in eval_result:
                result["total"] = eval_result["max_score"]
            if "avg_time" in eval_result:
                result["avg_time"] = round(eval_result["avg_time"], 2)

            # Mark as completed if we got valid results
            result["status"] = "completed"
            result["note"] = f"Evaluated on GAIA Level {level}"

            print(f"✓ Parsed results: {result['score']}/{result['total']} correct ({result['accuracy']}%)")
        else:
            print("✗ No results found in output")

    except FileNotFoundError:
        print(f"✗ Results file not found: {raw_results_path}")
        result["note"] = "Results file not found - evaluation may have failed"
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON in results file: {e}")
        result["note"] = f"Invalid results JSON: {e}"
    except Exception as e:
        print(f"✗ Error parsing results: {e}")
        result["note"] = f"Parser error: {e}"

    # Write output
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"✓ Leaderboard result written to: {output_path}")
    print(f"  Status: {result['status']}")
    print(f"  Accuracy: {result['accuracy']}%")

    return result


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: parse_results.py <raw_results.json> <output.json> <agent_image> <level> <task_ids>")
        sys.exit(1)

    raw_results_path = sys.argv[1]
    output_path = sys.argv[2]
    agent_image = sys.argv[3]
    level = int(sys.argv[4])
    task_ids = sys.argv[5]

    parse_results(raw_results_path, output_path, agent_image, level, task_ids)

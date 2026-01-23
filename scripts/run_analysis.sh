#!/bin/bash

# Analysis & AI Consulting OS - Pipeline Runner
# Orchestrates the complete 5-stage analysis pipeline

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
CONFIG_FILE="config.yaml"
OUTPUT_DIR="output"
LOG_FILE="$OUTPUT_DIR/analysis_$(date +%Y%m%d_%H%M%S).log"

# Usage information
usage() {
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  -u, --use-case <name>    Specify use case (churn_analysis, web_analytics, etc.)"
    echo "  -d, --data <path>        Path to dataset"
    echo "  -s, --stage <stage>      Run specific stage only (1-5)"
    echo "  -c, --config <file>      Custom config file (default: config.yaml)"
    echo "  -o, --output <dir>       Output directory (default: output/)"
    echo "  -h, --help               Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 -u churn_analysis -d data/customers.csv"
    echo "  $0 -u web_analytics -d data/events.csv -s 2"
    exit 1
}

# Parse arguments
USE_CASE=""
DATA_PATH=""
STAGE="all"

while [[ $# -gt 0 ]]; do
    case $1 in
        -u|--use-case)
            USE_CASE="$2"
            shift 2
            ;;
        -d|--data)
            DATA_PATH="$2"
            shift 2
            ;;
        -s|--stage)
            STAGE="$2"
            shift 2
            ;;
        -c|--config)
            CONFIG_FILE="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

# Validation
if [ -z "$USE_CASE" ]; then
    echo -e "${RED}Error: Use case is required${NC}"
    usage
fi

if [ -z "$DATA_PATH" ]; then
    echo -e "${RED}Error: Data path is required${NC}"
    usage
fi

if [ ! -f "$DATA_PATH" ]; then
    echo -e "${RED}Error: Data file not found: $DATA_PATH${NC}"
    exit 1
fi

if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}Error: Config file not found: $CONFIG_FILE${NC}"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log
echo "Analysis started at $(date)" | tee -a "$LOG_FILE"
echo "Use case: $USE_CASE" | tee -a "$LOG_FILE"
echo "Data: $DATA_PATH" | tee -a "$LOG_FILE"
echo "-----------------------------------" | tee -a "$LOG_FILE"

# Function to run a stage
run_stage() {
    local stage_num=$1
    local stage_name=$2
    local prompt_file=$3
    
    echo -e "\n${BLUE}=== Stage $stage_num: $stage_name ===${NC}" | tee -a "$LOG_FILE"
    
    if [ ! -f "$prompt_file" ]; then
        echo -e "${YELLOW}Warning: Prompt file not found: $prompt_file${NC}" | tee -a "$LOG_FILE"
        echo -e "${YELLOW}Using fallback prompt${NC}" | tee -a "$LOG_FILE"
    fi
    
    # Display prompt location
    echo "Prompt: $prompt_file" | tee -a "$LOG_FILE"
    
    # Create stage output file
    local output_file="$OUTPUT_DIR/stage_${stage_num}_${stage_name}.txt"
    
    echo "Stage $stage_num: $stage_name" > "$output_file"
    echo "Timestamp: $(date)" >> "$output_file"
    echo "Prompt: $prompt_file" >> "$output_file"
    echo "---" >> "$output_file"
    
    if [ -f "$prompt_file" ]; then
        cat "$prompt_file" >> "$output_file"
    fi
    
    echo -e "${GREEN}✓ Stage $stage_num setup complete${NC}" | tee -a "$LOG_FILE"
    echo "Output: $output_file" | tee -a "$LOG_FILE"
}

# Run analysis pipeline
echo -e "\n${BLUE}Starting Analysis Pipeline${NC}\n" | tee -a "$LOG_FILE"

if [ "$STAGE" = "all" ] || [ "$STAGE" = "1" ]; then
    run_stage 1 "data_prep" "prompts/core/data_prep.md"
fi

if [ "$STAGE" = "all" ] || [ "$STAGE" = "2" ]; then
    run_stage 2 "core_analysis" "prompts/core/core_analysis.md"
fi

if [ "$STAGE" = "all" ] || [ "$STAGE" = "3" ]; then
    run_stage 3 "drilldown" "prompts/core/drilldown.md"
fi

if [ "$STAGE" = "all" ] || [ "$STAGE" = "4" ]; then
    run_stage 4 "actionization" "prompts/core/actionization.md"
fi

if [ "$STAGE" = "all" ] || [ "$STAGE" = "5" ]; then
    run_stage 5 "iteration" "prompts/core/iteration.md"
fi

# Load use case specific prompt
USE_CASE_PROMPT="prompts/use_cases/${USE_CASE}/PROMPT.md"
if [ -f "$USE_CASE_PROMPT" ]; then
    echo -e "\n${BLUE}=== Use Case: $USE_CASE ===${NC}" | tee -a "$LOG_FILE"
    echo "Loading: $USE_CASE_PROMPT" | tee -a "$LOG_FILE"
    
    cp "$USE_CASE_PROMPT" "$OUTPUT_DIR/use_case_prompt.md"
    echo -e "${GREEN}✓ Use case prompt loaded${NC}" | tee -a "$LOG_FILE"
else
    echo -e "${YELLOW}Warning: Use case prompt not found: $USE_CASE_PROMPT${NC}" | tee -a "$LOG_FILE"
fi

# Load checklist
CHECKLIST="checklists/${USE_CASE}_checklist.md"
if [ -f "$CHECKLIST" ]; then
    echo -e "\n${BLUE}=== Quality Checklist ===${NC}" | tee -a "$LOG_FILE"
    echo "Loading: $CHECKLIST" | tee -a "$LOG_FILE"
    
    cp "$CHECKLIST" "$OUTPUT_DIR/checklist.md"
    echo -e "${GREEN}✓ Checklist loaded${NC}" | tee -a "$LOG_FILE"
fi

# Summary
echo -e "\n${GREEN}=== Analysis Pipeline Complete ===${NC}" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "Output directory: $OUTPUT_DIR" | tee -a "$LOG_FILE"
echo "Log file: $LOG_FILE" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "Next steps:" | tee -a "$LOG_FILE"
echo "1. Review prompts in $OUTPUT_DIR/" | tee -a "$LOG_FILE"
echo "2. Copy prompts to your AI tool (ChatGPT, Claude, etc.)" | tee -a "$LOG_FILE"
echo "3. Paste your dataset when prompted" | tee -a "$LOG_FILE"
echo "4. Follow the 5-stage pipeline" | tee -a "$LOG_FILE"
echo "5. Use the checklist to validate results" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "Analysis completed at $(date)" | tee -a "$LOG_FILE"

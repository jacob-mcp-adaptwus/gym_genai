#!/bin/bash
# print_project_docs.sh - Script to print contents of project documentation and configuration files

# Default output file
OUTPUT_FILE="project_files.txt"

# Colors for terminal output
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color
SEPARATOR='================================================================'

# Function to print a header
print_header() {
    echo -e "\n$SEPARATOR"
    echo -e "File: $1"
    echo -e "Type: $2"
    echo -e "$SEPARATOR\n"
}

# Arrays of file patterns to match
doc_extensions=("md" "txt" "rst" "adoc" "markdown")
code_extensions=("py" "sh" "js" "ts" "jsx" "tsx" "vue")
config_files=(
    "Dockerfile"
    "docker-compose.yml"
    "docker-compose.yaml"
    ".env"
    ".env.example"
    ".gitignore"
    "requirements.txt"
    "package.json"
    "setup.py"
    "config.py"
    "*.conf"
    "*.config.js"
    "*.toml"
    "*.yaml"
    "*.yml"
    "nginx.conf"
    "*.ini"
)

# Function to process files
process_files() {
    local file="$1"
    local type="$2"
    
    # Skip binary files and empty files
    if [ -f "$file" ] && [ -s "$file" ] && file "$file" | grep -q "text"; then
        # Print the header with the file path
        print_header "$file" "$type"
        
        # Print file contents
        cat "$file"
        
        # Print a separator
        echo -e "\n$SEPARATOR\n"
    fi
}

# Clear or create the output file
echo "Starting project file analysis..." > "$OUTPUT_FILE"

# Find all relevant files
find . \
    -not -path '*/\.*' \
    -not -path '*/node_modules/*' \
    -not -path '*/venv/*' \
    -not -path '*/env/*' \
    -not -path '*/build/*' \
    -not -path '*/dist/*' \
    -not -path '*/__pycache__/*' \
    -type f \
    | sort \
    | while read -r file; do
        # Get the file extension and basename
        filename=$(basename "$file")
        extension="${file##*.}"
        
        # Check documentation files
        for doc_ext in "${doc_extensions[@]}"; do
            if [ "$extension" = "$doc_ext" ]; then
                process_files "$file" "Documentation" >> "$OUTPUT_FILE"
                continue 2
            fi
        done
        
        # Check code files
        for code_ext in "${code_extensions[@]}"; do
            if [ "$extension" = "$code_ext" ]; then
                process_files "$file" "Code" >> "$OUTPUT_FILE"
                continue 2
            fi
        done
        
        # Check configuration files
        for config_pattern in "${config_files[@]}"; do
            if [[ "$filename" == $config_pattern ]] || [[ "$file" == *"$config_pattern" ]]; then
                process_files "$file" "Configuration" >> "$OUTPUT_FILE"
                continue 2
            fi
        done
done

# Add completion message to the file
echo "File printing complete!" >> "$OUTPUT_FILE"
echo "Note: Some binary files may have been skipped" >> "$OUTPUT_FILE"

# Print success message to terminal
echo -e "${GREEN}Output has been saved to: $OUTPUT_FILE${NC}"
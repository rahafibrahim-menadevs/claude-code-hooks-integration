import json
import sys
from pathlib import Path
from datetime import datetime, timezone

class HookReceiver:
    def read_event(self):
        try:
            event = json.load(sys.stdin)

            if not isinstance(event, dict):
                raise ValueError("Expected a JSON object")

            return event
        
        except json.JSONDecodeError:
             raise ValueError("Invalid JSON input")


class EventLogger:
    def __init__(self, file_path="ClaudeEvents.jsonl"):
        self.file_path = Path(file_path)

    def save_event(self, event):
        log_entry = event.copy()
        log_entry["captured_at"] = datetime.now(timezone.utc).isoformat()

        with open(self.file_path, "a", encoding="utf-8") as file:
            json.dump(log_entry, file, ensure_ascii=False)
            file.write("\n")

def main():
    try:
        receiver = HookReceiver()
        logger = EventLogger()

        event = receiver.read_event()
        logger.save_event(event)

    except (ValueError, OSError) as error:
        print(f"Hook logging error: {error}", file=sys.stderr)

# the following two lines run main() when this script is executed directly, they are optionally added and could be removed.
if __name__ == "__main__":
    main() 



    

    






        


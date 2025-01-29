def solution(video_len: str, pos: str, op_start: str, op_end: str, commands: list) -> str:
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(":"))
        return minutes * 60 + seconds

    def seconds_to_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    video_length = time_to_seconds(video_len)
    position = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)


    for command in commands:
        if op_start_sec <= position <= op_end_sec:  
            position = op_end_sec
            
        if command == "prev":
            position = max(0, position - 10)
        elif command == "next":
            position = min(video_length, position + 10)
            
        if op_start_sec <= position <= op_end_sec:  
            position = op_end_sec


    return seconds_to_time(position)

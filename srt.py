from youtube_transcript_api import YouTubeTranscriptApi
import re
from youtube_transcript_api.formatters import SRTFormatter

# assigning srt variable with the list of dictionaries
# obtained by the .get_transcript() function
# and this time it gets only the subtitles that
# are of english language.


def extract_video_id(url):
    # Extract video ID from the YouTube URL
    regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.{11})"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        return None


def change(link, name, path):
    if extract_video_id(link):
        srt = YouTubeTranscriptApi.get_transcript(str(extract_video_id(link)),
                                                  languages=['en'])
        formatter = SRTFormatter()
        json_formatted = formatter.format_transcript(srt)
        # prints the result
        with open(f'{path}/{name}.srt', 'w', encoding='utf-8') as json_file:
            json_file.write(json_formatted)
            return srt
    return


if __name__ == "__main__":
    change(input("link: "), input("Name: "),
           "/home/udoka/chuks/CS50_W/Louis/LAB/ML_LAB/cars/youtube")

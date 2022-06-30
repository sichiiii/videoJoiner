from moviepy.editor import *


def concatenate(video_clip_paths, output_path, method="compose"):
    clips = [VideoFileClip(c) for c in video_clip_paths]
    if method == "reduce":
        min_height = min([c.h for c in clips])
        min_width = min([c.w for c in clips])
        clips = [c.resize(newsize=(min_width, min_height)) for c in clips]
        final_clip = concatenate_videoclips(clips)
    elif method == "compose":
        final_clip = concatenate_videoclips(clips, method="compose")

    final_clip.write_videofile(output_path)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--clips", nargs="+",
                        help="List of audio or video clip paths")
    parser.add_argument("-r", "--reduce", action="store_true",
                        help="Whether to use the `reduce` method to reduce to the lowest quality on the resulting clip")
    parser.add_argument("-o", "--output", help="Output file name")
    args = parser.parse_args()
    clips = args.clips
    output_path = args.output
    reduce = args.reduce
    method = "reduce" if reduce else "compose"
    concatenate(clips, output_path, method)

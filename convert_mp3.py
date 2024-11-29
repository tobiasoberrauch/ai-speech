import os
from pydub import AudioSegment

def resample_mp3(input_path, output_dir, target_sample_rate=16000):
    # Load the audio file
    audio = AudioSegment.from_mp3(input_path)
    
    # Create output filename
    basename = os.path.basename(input_path)
    output_path = os.path.join(output_dir, basename)
    
    # Check current sample rate
    if audio.frame_rate != target_sample_rate:
        # Resample the audio
        audio = audio.set_frame_rate(target_sample_rate)
        
        # Export the resampled audio
        audio.export(output_path, format="mp3")
        print(f"Resampled {basename} to {target_sample_rate}Hz")
    else:
        # Even if same rate, copy to output dir for consistency
        audio.export(output_path, format="mp3")
        print(f"Copied {basename} - already at {target_sample_rate}Hz")

def process_directory(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Process all MP3 files in input directory
    for file in os.listdir(input_dir):
        if file.lower().endswith('.mp3'):
            input_path = os.path.join(input_dir, file)
            resample_mp3(input_path, output_dir)

if __name__ == "__main__":
    input_dir = "./use-cases/flemish/raw"
    output_dir = "./use-cases/flemish/16k"
    print(f"Processing MP3 files from {input_dir} to {output_dir}")
    process_directory(input_dir, output_dir)
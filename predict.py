# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

import os
import time
import subprocess
import nemo.collections.asr as nemo_asr
from cog import BasePredictor, Input, Path

PARAKEET_WEIGHTS_CACHE = "./weights"
PARAKEET_WEIGHTS_URL = "https://weights.replicate.delivery/default/Parakeet/parakeet-rnnt-1.1b.tar"
PATH_TO_PARAKEET = "./weights/parakeet-rnnt-1.1b.nemo"


def download_weights(url, dest):
    start = time.time()
    print("downloading url: ", url)
    print("downloading to: ", dest)
    subprocess.check_call(["pget", "-x", url, dest], close_fds=False)
    print("downloading took: ", time.time() - start)


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""

        if not os.path.exists(PARAKEET_WEIGHTS_CACHE):
            download_weights(PARAKEET_WEIGHTS_URL, PARAKEET_WEIGHTS_CACHE)
        self.asr_model = nemo_asr.models.EncDecRNNTBPEModel.restore_from(PATH_TO_PARAKEET)

    def predict(self, audio_file: Path = Input(description="Input audio file to be transcribed by the ASR model"),) -> str:
        """Transcribes the input audio file using the ASR model and returns the transcription as a string"""

        # The model returns a tuple of lists, each containing a single string (transcription)
        transcription = self.asr_model.transcribe([str(audio_file)])
        if transcription and transcription[0]:
            return transcription[0][0]
        else:
            print("Error: Transcription failed or returned empty result.")
            return ""

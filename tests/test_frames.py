from pathlib import Path
import sys
import pytest
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from agf_tools.frames import center_rgba_frame, preview_gif

def test_alpha(tmp_path):
    source = tmp_path / "in.png"
    output = tmp_path / "out.png"
    Image.new("RGBA", (4, 4), (255, 0, 0, 100)).save(source)
    center_rgba_frame(source, output, (8, 8))
    with Image.open(output) as im:
        assert im.size == (8, 8)
        assert im.getpixel((0, 0))[3] == 0
        assert im.getpixel((3, 3))[3] == 100

def test_refuses_crop(tmp_path):
    source = tmp_path / "in.png"
    Image.new("RGBA", (8, 8)).save(source)
    with pytest.raises(ValueError):
        center_rgba_frame(source, tmp_path / "out.png", (4, 4))

def test_gif(tmp_path):
    frames = []
    for i in range(2):
        path = tmp_path / f"{i}.png"
        Image.new("RGBA", (8, 8), (i * 255, 0, 0, 255)).save(path)
        frames.append(path)
    output = tmp_path / "out.gif"
    preview_gif(frames, output)
    with Image.open(output) as im:
        assert im.n_frames == 2

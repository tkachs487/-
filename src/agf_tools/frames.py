from pathlib import Path
from PIL import Image

def center_rgba_frame(source: Path, output: Path, canvas: tuple[int, int]) -> None:
    """Center a sprite on a transparent canvas; refuse cropping."""
    with Image.open(source) as img:
        sprite = img.convert("RGBA")
        if sprite.width > canvas[0] or sprite.height > canvas[1]:
            raise ValueError("Frame exceeds canvas: cropping refused")
        result = Image.new("RGBA", canvas, (0, 0, 0, 0))
        result.alpha_composite(sprite, ((canvas[0] - sprite.width) // 2, (canvas[1] - sprite.height) // 2))
        output.parent.mkdir(parents=True, exist_ok=True)
        result.save(output)

def preview_gif(frames: list[Path], output: Path, duration_ms: int = 100) -> None:
    """Create an animation preview from equally sized PNG frames."""
    if not frames or duration_ms <= 0:
        raise ValueError("Frames and positive duration required")
    images = []
    try:
        for path in frames:
            with Image.open(path) as im:
                images.append(im.convert("RGBA"))
        if len({im.size for im in images}) != 1:
            raise ValueError("All frames must have identical dimensions")
        output.parent.mkdir(parents=True, exist_ok=True)
        images[0].save(output, save_all=True, append_images=images[1:], duration=duration_ms, loop=0, disposal=2)
    finally:
        for im in images:
            im.close()

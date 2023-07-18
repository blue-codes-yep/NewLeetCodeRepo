class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # If the color of the starting pixel is already the new color, return the image as is.
        if image[sr][sc] == newColor:
            return image

        # Otherwise, start the flood fill process.
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image

    def fill(self, image, sr, sc, color, newColor):
        # If this pixel is out of bounds or not the old color, we return without doing anything.
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color:
            return
        
        # We change the color of the current pixel.
        image[sr][sc] = newColor

        # Then we attempt to color the pixels to the north, south, east, and west of the current pixel.
        self.fill(image, sr - 1, sc, color, newColor)  # North
        self.fill(image, sr + 1, sc, color, newColor)  # South
        self.fill(image, sr, sc - 1, color, newColor)  # West
        self.fill(image, sr, sc + 1, color, newColor)  # East

package garden.tiles;

import java.util.Objects;

import garden.colours.Colours;

public class StoneTile extends Tile {
    public StoneTile(boolean glossy) {
        super("Stone Tile", Colours.GRAY, glossy);  // Specific properties for Stone Tile
    }

    @Override
    public String colour(int season) {
        return super.colour(season);  // Utilizes the Tile's colour implementation, including glossiness
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof StoneTile)) return false;
        return super.equals(obj);  // Leveraging Tile's equals implementation
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}

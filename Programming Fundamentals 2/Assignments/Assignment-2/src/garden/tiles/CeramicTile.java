package garden.tiles;

import java.util.Objects;

import garden.colours.Colours;

public class CeramicTile extends Tile {
    public CeramicTile(boolean glossy) {
        super("Ceramic Tile", Colours.RED, glossy);  // Specific properties for Ceramic Tile
    }

    @Override
    public String colour(int season) {
        return super.colour(season);  // Utilizes the Tile's colour implementation, including glossiness
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof CeramicTile)) return false;
        return super.equals(obj);  // Leveraging Tile's equals implementation
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}

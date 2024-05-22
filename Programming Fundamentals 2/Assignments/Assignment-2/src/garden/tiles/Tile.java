package garden.tiles;

import java.util.Objects;
import garden.Ornament;

/**
 * Represents a Tile, with a specific name, color and boolean glossy value
 * This class extends the Ornament interface
 */
public class Tile implements Ornament {
    private String name;
    private String color;
    private boolean glossy;

    // Constructs a Tile instance with the specific attributes
    public Tile(String name, String color, boolean glossy) {
        this.name = name;
        this.color = color;
        this.glossy = glossy;
    }

    // Returns the color of the tile, surrounded by parantheses if tile is glossy
    @Override
    public String colour(int season) {
        return glossy ? "(" + color + ")" : color;
    }

    // Returns Name of the tile
    @Override
    public String getName() {
        return name;
    }
    
    // Checks if tile is equal ot another by comparing name, color and glossiness
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Tile other = (Tile) obj;
        return Objects.equals(name, other.name) &&
               Objects.equals(color, other.color) &&
               glossy == other.glossy;
    }

    // Returns hash value for tile based on color, name and glossiness
    @Override
    public int hashCode() {
        return Objects.hash(name, color, glossy);
    }
}

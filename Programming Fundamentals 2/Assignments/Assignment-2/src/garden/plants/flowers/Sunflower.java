package garden.plants.flowers;

import java.util.Objects;
import garden.colours.*;

public class Sunflower extends Flower {
    public Sunflower(String color) {
        super("Sunflower", 0.5, Colours.BROWN, color, color, Colours.GREEN); // Initialize with specific characteristics for Sunflowers
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Sunflower)) return false;
        return super.equals(obj); // Leveraging the Flower's equals implementation
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}

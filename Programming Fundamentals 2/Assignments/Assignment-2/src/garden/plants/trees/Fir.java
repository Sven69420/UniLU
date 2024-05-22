package garden.plants.trees;

import java.util.Objects;

import garden.colours.Colours;

public class Fir extends Tree {
    public Fir() {
        super("Fir", 30, Colours.GREEN, Colours.GREEN, Colours.GREEN, Colours.GREEN, null);  // Fir's colors do not change across seasons
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Fir)) return false;
        return super.equals(obj);  // Leveraging Tree's equals implementation
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}

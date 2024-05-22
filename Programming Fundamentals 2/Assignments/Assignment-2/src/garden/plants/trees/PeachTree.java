package garden.plants.trees;

import java.util.Objects;

import garden.colours.Colours;

public class PeachTree extends Tree {
    public PeachTree() {
        super("Peach Tree", 35, Colours.BROWN, Colours.PINK, Colours.GREEN, Colours.YELLOW, "Peach");  // Peach Tree's specific characteristics
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof PeachTree)) return false;
        return super.equals(obj);  // Leveraging Tree's equals implementation
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}

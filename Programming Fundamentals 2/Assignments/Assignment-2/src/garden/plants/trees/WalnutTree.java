package garden.plants.trees;

import java.util.Objects;

public class WalnutTree extends Tree {
    public WalnutTree() {
        super("Walnut Tree", 20, "Brown", "Green", "Green", "Yellow", "Walnut");  // Walnut Tree's specific characteristics
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof WalnutTree)) return false;
        return super.equals(obj);  // Leveraging Tree's equals implementation
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}

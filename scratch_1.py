if (a1.x - b.x) ** 2 + (a2.y - b.y) ** 2 <= circ1.radius ** 2:
    vector_a1_b = b.x * b.y - a1.x * a1.y
    a1.velocity = normalized(vector_a1_b) * vector_a1_b.velocity.magnitude

a1.x += a1.velocity.x
a1.y += a1.velocity.y
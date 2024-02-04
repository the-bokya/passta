# Purpose

This provides a secure mode of password generation. The generation is deterministic, meaning if the initial inputs for generation are the same, `passta` will always generate the same password. This generator works on the principle that the inital conditions provided to it are provided to it as seed input. As an experiment, try changing the length by one. The entire password changes. Now change it back.

# Usage

- `length`: Sets the length of the output password.
- `password`: This is a human-readable password you carry around in your head. We made this program just because you entered this password every damn where. Example: your name.
- `salt`: A string to further randomize the generator. Ideally this should change for each new application. Example: the name of your current crush.

# Demo

Now, when I enter the initial conditions:



```
Enter the length of the password to be generated: 32
Enter your password: mitsuha
Enter salt: taki
```

I get this password: `zS)RNE;^*}9t1GmKpx!'o-""J7bBsIcY`

# Note

In early stages, **do not use. AT ALL!**. This is because the program is still in development and breaking changes in the generation mechanism will mean your password is lost into the abyss of probability.

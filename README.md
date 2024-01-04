# Jinja: NeverUndefined

End the lawless era of Jinja.

`NeverUndefined` is more restrictive than `StrictUndefined`. See [this issue](https://github.com/pallets/jinja/issues/1923).

## Usage

1. Install the package:

    ```bash
    pip3 install jinja2_neverundefined
    ```

2. Create a template file named `template.j2` with the following content:

    ```jinja
    {% macro test(a, b, c) %}
    a macro with three parameters but not used
    {%endmacro%}

    {{test()}}
    ```

3. Create a Python script named `example.py` with the following content:

    ```python
    from jinja2 import Environment, FileSystemLoader
    from jinja2_neverundefined import NeverUndefined

    # Create Jinja2 environment with the extension
    env = Environment(
        loader=FileSystemLoader('.'),
        undefined=NeverUndefined
    )

    # Render the template
    template = env.get_template('template.j2')
    rendered = template.render()

    # Print the rendered output
    print(rendered)
    ```

4. Run the script:

    ```bash
    python3 example.py
    ```

The script will raise an exception because parameters `a b c` are not provided when calling macro `test` in the template.

By using the `NeverUndefined` extension, the Jinja environment will raise an exception when encountering an undefined variable. This helps catch potential issues or missing variable bindings in your templates.
# Portfolio Site
Daniel Corcoran's static portfolio website, currently being hosted on github pages and generated via `jupyter notebook`. This is an enduring piece and is to be updated regularly as projects are completed. 

The main reason for the creation of this website was to bring together Daniel Corcoran's projects from a range of disparate sources such as **Wordpress**, **Github** and **Tableau**.

The site can currently be visitted using this [link](https://danielc92.github.io/portfolio-site/).

# Setup
This project currently relies on the use of `jupyter notebook` in `python3.7`. No additional libraries are used except for some inbuilt python libraries.

```sh
pip install jupyter
pip install jinja2
```

Obtaining the repository
```sh
git clone https://gitlab.com/corcoran/portoflio.git
```

# Instructions
```
python gen.py
```

Within the notebook it is split up into several components.
1. Base templates - Sets up 'base templates' or otherwise static code within the website that does not change that often, such as the `<head>` and `<footer>`. 
2. Data - Currently hard-coded data which is iteratively fed into the templates for the website, these contain project information.
3. Build Projects - Builds the project section of the website by iterating through the data in step **2**.
4. Generate Site - Consolidates all variables within the notebook into one string, representing the website.
5. Export to html - This step is required to export the python string representation of the site into an `.html` file so that github is able to host it.

# Contributors
- Daniel Corcoran

# Tests
- `Bootstrap` css framework applied and working as intended.
- `google fonts` applied and working as intended.
- Feeding data into project base template, all images and text appear in html as intended.
- Site exports successully.
- Site runs successfully on github pages.
- Site links, images are working as intended.

# Sources
- [Bootstrap templates](https://startbootstrap.com/template-categories/all/)
- [Hosting on Github Documentation](https://pages.github.com/)
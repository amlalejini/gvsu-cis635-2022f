# tidyverse

From the [tidyverse website](https://www.tidyverse.org):

> The tidyverse is an opinionated collection of R packages designed for data science.
> All packages share an underlying design philosophy, grammar, and data structures.

The tidyverse includes the following packages:

- [ggplot2](https://ggplot2.tidyverse.org/) - provides a system for creating graphics based on [The Grammar of Graphics](https://ezproxy.gvsu.edu/login?url=https://search.ebscohost.com/login.aspx?direct=true&AuthType=ip,sso&db=cat08964a&AN=gvsu.ebs286449e&site=eds-live&scope=site)
- [dplyr](https://dplyr.tidyverse.org/) - provides functions for data manipulation
- [tidyr](https://tidyr.tidyverse.org/) - provides functions that help you turn your data into [_tidy_ data](https://tidyr.tidyverse.org/articles/tidy-data.html)
- [readr](https://readr.tidyverse.org/) - provides fast functions for reading data from files
- [forcats](https://forcats.tidyverse.org/) - provides functions for working with factors
- [tibble](https://tibble.tidyverse.org/) - provides an alternative data structure (a tibble) to the data frame
- [stringr](https://stringr.tidyverse.org/) - provides functions for working with strings
- [purrr](https://purrr.tidyverse.org/) - provides tools for working with functions and vectors

Install the tidyverse collection of packages using:

```
install.packages("tidyverse")
```

While all of the tidyverse is useful for working with data (and worth spending time to learn),
we'll focus on the dplyr, tidyr, and ggplot2 packages.
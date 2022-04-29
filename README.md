# bio_analysis
This project is a group assignment for 9785 in University of Canberra, which is related to data analysis. Specifically, it will analysis data generated by other bioanalytical software such as [Roary](https://sanger-pathogens.github.io/Roary/).

The steps of analysis includes: 

- Data Extraction
- Data pre-processing
- Visualization(venn diagram, upsetplot)

Many excellent Python open source libraries are used in the project for data analysis, such as Pandas, Numpy and Matplotlib. Meanwhile, [pyvenn](https://github.com/tctianchi/pyvenn) and [UpSetPlot](https://upsetplot.readthedocs.io/en/stable/) make great contribution to the visulization. 

Great appreciation to these authors for contributing these excellent and convenient open source libraries.

## future improvement
As the primary developer of our final capstone data analysis project, It is obvious there are various aspects of our project that can be improved. Firstly, the function of human-computer interaction in the project is not good enough. We should have put more effort in this part, although it is a CLI program. For further development, if time permits, we may add some functions that allow users to modify the attribute(figure size, colour, title...) of the diagram depicted by our software and the path where the output images are stored. In addition, it is also useful to develop a bash script as a mechanism for the interaction between users and our software, instead of blocking the user at runtime waiting for their commands, which also facilitates parallelism. Another valuable point to enhance is the user-friendly document. Some UNIX-like command formats and description can be explained in the user doc. It allows users to get started with our software more easily.

# joyce-word-dictionary

The Joyce Word Dictionary, a rewrite of joycewords.com. Work in progress.

[See the work-in-progress development website here, on Netlify.](http://joyce-words.netlify.com)

## Description of JWD 1.0

Here's Natasha Chenier and James O'Sullivan, from their article in James Joyce Quarterly (Volume 53, Number 1-2, Fall 2015-Winter 2016, pp. 17-21): 

James Joyce invented thousands of words, most of which have yet to be thoroughly defined or analyzed, and many still elude understanding. The online and open access Joyce Word Dictionary (JWD) aims to provide a space in which readers, scholars, and lexicographers around the world can explore Joyce’s elaborate contribution to literature and language. Rather than being a conventional dictionary, which assumes an authoritative role in the definition of words, the open access JWD enables multiple word meanings democratically to co-exist. Meanings will constantly be changing and developing with the help of all who wish to contribute.

From a technical perspective, the dictionary currently functions as a self-hosted Wordpress installation. Using a platform like Wordpress means that the user-centered aspects of the site can be maintained with greater ease and fewer resources. The current beta version of the site will be improved, particularly in relation to the interface through which users navigate through the neologisms. The site’s current lack of responsive interface will also be addressed, so that the resource can be utilized more efficiently on mobile devices. The data itself is held in CSV format, so that it is sustainable and flexible—it can be readily ported to different systems, as well as shared with external users and platforms, as required. Currently, this data is managed in a Wordpress plugin that has been tailored to suit user purposes, providing an intuitive interface through which the relevant editors might add new content without having to interact directly with the underlying CSV file.

There are several challenges specific to this project’s digital aspects that will need to be addressed in the longer term. As already noted, a more robust and intuitive platform will need to be put in place. The portability of the resource’s data structures are such that the foundations for a purpose-built environment are already in place, but decisions are yet to be taken on a number of essential processes. For example, whether the site should operate as a group- or crowd- sourced project needs to be considered, as do the editorial repercus- sions of varying strategies. Since the project is digital, the scope for a federated policy, wherein contributors present sets of alternative definitions, should be explored. The JWD presents ample opportunities for the embedding of analytical features, facilitating macro-level interactions in a way that better integrates its content so that it is more accessible and intuitive to users. From a technical perspective, this project is very much in its infancy, but the content—where the entirety of the project’s value is to be found—is quickly developing. The means through which that content can best be stored, disseminated, and interrogated will form a major part of the project’s next phase.

## Contributing

The Joyce Word Dictionary (JWD) 2.0 is built using: 

 - [Eleventy](http://11ty.io), a static site generator
 - [Pug Templates](https://github.com/pugjs/pug)
 - [Sass](http://sass-lang.com/)

The words themselves are stored [in this YAML file](https://github.com/open-editions/joyce-word-dictionary/blob/master/src/data/words.yaml). Feel free to add an entry, and submit a pull request, as a stopgap measure before we build our submission system.

If you see a problem with the website or its content, feel free to open a new issue. 

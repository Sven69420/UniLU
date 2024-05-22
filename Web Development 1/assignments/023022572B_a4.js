function imageReport(){
    // initialize counters for different image porperties
    let total = 0;
    let measured = 0;
    let accessible = 0;
    let responsive = 0;
    let external = 0;

    // get all image elements in the given HTML document
    const images = document.querySelectorAll('img');

    // increase total amount based on images in HTML document
    for (const image of images){
        total++;

        // check if image has width and height attributes and increase measured count
        if (image.hasAttribute('width') && image.hasAttribute('height')){
            measured++;
        }

        // check if the image has an alt accessibility attribute
        if (image.hasAttribute('alt') && image.getAttribute('alt').trim() !== ''){
            accessible++;
        }

        // check if the image has an attribute or class indicating if its responsive
        if (image.hasAttribute('srcset')){
            responsive++;
        }

        // check if the image is loaded from an external domain
        const src = image.getAttribute('src');
        if (src){
            // gets the current hostname of the webpage
            const currentHost = window.location.hostname;
            // create a url object for the image source
            const url = new URL(src, window.location.origin);
            // extract the hostname of the image source
            const imageHost = url.hostname;

            // if image source hostname is different from current hostname, increase external count
            if (imageHost !== currentHost){
                external++;
            }
        }
    }
    // create image report list with all iterated counters in it
    const imgReport = {
        total,
        measured,
        accessible,
        responsive,
        external,
    };
    // returns completed image report with all updated counters
    return imgReport;
};
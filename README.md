## Getting Started
```bash
git clone git@github.com:hweej/htan-vitessce-proto.git
cd htan-vitessce-proto
```
```bash
npm install 
# or
yarn install
```

## Start Frontend Server
First, run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.


## Build example data
Run the `make` commands from `data/visium_10x/Makefile`
```bash
cd data/visium_10x
make all
conda activate vitessce-tutorial-env
make install  # Build the example datafiles 
```

## Start data-server 
Simple http-server to serve zarr files
```bash
# Return to project root and run:
make data-server
# or
http-server ./data/visium_10x --cors -p 9002
```

## Learn More about NextJS
You can start editing the page by modifying `pages/index.js`. The page auto-updates as you edit the file.

[API routes](https://nextjs.org/docs/api-routes/introduction) can be accessed on [http://localhost:3000/api/hello](http://localhost:3000/api/hello). This endpoint can be edited in `pages/api/hello.js`.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.


To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

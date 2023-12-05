FROM node:18.18.2-alpine as frontutopia

WORKDIR /usr/src/app

# Copy only package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies as root
RUN npm install -g npm@10.2.4 serve vite && npm install

# Copy the rest of the application files
COPY . .

# Expose the port
EXPOSE 80

# Start the application
# TODO: Change this to production and run as non-root)
CMD ["npm", "run", "dev"]
# RUN npm run build && cd dist
# CMD ["serve", "-p", "80"]
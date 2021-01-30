node {
    // Mark the code checkout 'stage'....
    stage 'Checkout'

    // Get the code from a GitHub repository
    git credentialsId: 'mycredentials', url: 'https://github.com/<user>/<project>/'

    // Mark the code build 'stage'....
    stage 'Build'

    // Get the venv
    env.PATH="${env.WORKSPACE}/venv/bin:/usr/bin:${env.PATH}"

    // Intalling requirements in venv
    sh "${env.WORKSPACE}/venv/bin/pip install -r requirements.txt"

    // Start the tests
    stage 'Test'
    sh "${env.WORKSPACE}/venv/bin/python34 manage.py test"
}
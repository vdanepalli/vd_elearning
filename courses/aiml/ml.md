# [Machine Learning](../../courses.md)

- [Machine Learning](#machine-learning)
  - [Google: Machine Learning Crash Course](#google-machine-learning-crash-course)
    - [Introduction](#introduction)
  - [LLM: Machine Learning](#llm-machine-learning)
    - [Linear Algebra](#linear-algebra)


## Google: Machine Learning Crash Course

### Introduction

- ML -- train a piece of software called model (mathematical relationship derived from data) to make useful predictions or generate content
- Supervised - how data maps to correct answers
  - Regression -- predict numeric value
  - Classification -- predict a class/category
    - Binary 
    - Multi-class
  - concepts
    - Datasets are made up of individual examples that contain features and a label
      - size - number of examples 
      - diversity - range the examples cover
      - features 
    - Model
- Unsupervised -- identify patterns in data
  - Clustering
- Reinforcement -- predictions by getting rewards/penalties based on actions within an environment
  - generates a policy that defines strategy for getting most rewards
- Generative AI - class of models creating content
  - learn patterns in data with the goal to produce new but similar data
  - model learns to mimic the data it's trained on
  - trained as unsupervised, then optionally as supervised or reinforcement


## LLM: Machine Learning 

### Linear Algebra

Scalars: 
- single numeric value, magnitude, quantity, point in 1D scale. 
- how much or how many --- int, float, double, feature values, hyperparameters, weights, biases
- No direction or spatial relationships

Vectors:
- both magnitude and direction
- ordered list of numbers (row or col) (components or elements corresponding to the vector's projection onto axes of a coordinate system)
- N-dimensional space (represented by $\mathbb{R}^N$)
- magnitude/length/norm is calculated by generalized Pythogorean theorem (L2 norm) denoted by $\| \mathbf{v} \|_2 = \sqrt{v_1^2 + v_2^2 + \dots + v_N^2}$
- `magnitude_2d = np.linalg.norm(vector_2d)`



<br/><br/>


Matrices:
- ordered rectangular grid of numbers
- rows -- items/observations; cols -- attributes/features
- represent linear transformations -- take vector as input and transform it into another vector preserving vector addition and scalar multiplication -- Additivity and Homogeneity
  - types: Rotation (rotate around origin), Scaling (stretch/compress), Shearing (shift a vector along one axis depending on its position along other), Projection


Breakfast:
- required 
  1. 30-35g protein
  2. 30-45g carbs
  3. 10-25g fat
- option 1:
  - Protein Powder + Water
  - 2 Tbsp Chia seeds
  - 1 Banana
- option 2:
  - 4 Hardboiled Eggs
  - 1/2 cup cooked quinoa + 1 Tbsp milled flax




Lunch: 
- required
  - 40-50g protein
  - 60-80g carbs
  - 5-10g fat
- option 1: 
  - cooked chicken 140g uncooked
  - cooked grain 1.5 cups
  - vegetables steamed 1.5 cups



Dinner:
- required
  - 45-55g protein
  - 70-90g carbs
  - 15-30g fat
- option 1:
  - cooked chicken or eggs
  - cooked rice or quinoa or potatoes
  - cooked/fresh vegetables
  - cooking oil



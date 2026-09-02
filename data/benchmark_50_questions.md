# Medical RAG 50-Question Benchmark Dataset Study Guide

This document contains the curated set of **50 clinical evaluation questions** randomly sampled exclusively from the **Top 3 Focus Areas** (`Breast Cancer`, `Prostate Cancer`, `Stroke`) in `gold_data.csv`.

## 1. Focus Area Distribution Overview

| Focus Area | Question Count | Percentage |
|---|---|---|
| **Breast Cancer** | 21 | 42.0% |
| **Prostate Cancer** | 16 | 32.0% |
| **Stroke** | 13 | 26.0% |

---

## 2. Quick Reference Table

| # | QID | Focus Area | Source | Question |
|---|---|---|---|---|
| 01 | `q505` | Stroke | NIHSeniorHealth | What is (are) Stroke ? |
| 02 | `q394` | Breast Cancer | NIHSeniorHealth | Who is at risk for Breast Cancer? ? |
| 03 | `q188` | Prostate Cancer | NIHSeniorHealth | What are the treatments for Prostate Cancer ? |
| 04 | `q385` | Breast Cancer | NIHSeniorHealth | What are the treatments for Breast Cancer ? |
| 05 | `q1311` | Prostate Cancer | CancerGov | Who is at risk for Prostate Cancer? ? |
| 06 | `q506` | Stroke | NIHSeniorHealth | What are the symptoms of Stroke ? |
| 07 | `q519` | Stroke | NIHSeniorHealth | What is (are) Stroke ? |
| 08 | `q1170` | Prostate Cancer | CancerGov | What is the outlook for Prostate Cancer ? |
| 09 | `q773` | Breast Cancer | CancerGov | How to diagnose Breast Cancer ? |
| 10 | `q195` | Prostate Cancer | NIHSeniorHealth | Who is at risk for Prostate Cancer? ? |
| 11 | `q1160` | Breast Cancer | CancerGov | Is Breast Cancer inherited ? |
| 12 | `q381` | Breast Cancer | NIHSeniorHealth | What is (are) Breast Cancer ? |
| 13 | `q514` | Stroke | NIHSeniorHealth | What is (are) Stroke ? |
| 14 | `q173` | Prostate Cancer | NIHSeniorHealth | What are the treatments for Prostate Cancer ? |
| 15 | `q1162` | Breast Cancer | CancerGov | How to diagnose Breast Cancer ? |
| 16 | `q1165` | Breast Cancer | CancerGov | What are the treatments for Breast Cancer ? |
| 17 | `q390` | Breast Cancer | NIHSeniorHealth | What is (are) Breast Cancer ? |
| 18 | `q772` | Breast Cancer | CancerGov | What are the symptoms of Breast Cancer ? |
| 19 | `q1158` | Breast Cancer | CancerGov | Who is at risk for Breast Cancer? ? |
| 20 | `q776` | Breast Cancer | CancerGov | What are the treatments for Breast Cancer ? |
| 21 | `q187` | Prostate Cancer | NIHSeniorHealth | What are the treatments for Prostate Cancer ? |
| 22 | `q179` | Prostate Cancer | NIHSeniorHealth | What causes Prostate Cancer ? |
| 23 | `q8466` | Stroke | NHLBI | Who is at risk for Stroke? ? |
| 24 | `q180` | Prostate Cancer | NIHSeniorHealth | Who is at risk for Prostate Cancer? ? |
| 25 | `q9263` | Stroke | NINDS | What is (are) Stroke ? |
| 26 | `q399` | Breast Cancer | NIHSeniorHealth | What are the treatments for Breast Cancer ? |
| 27 | `q520` | Stroke | NIHSeniorHealth | What is (are) Stroke ? |
| 28 | `q770` | Breast Cancer | CancerGov | What is (are) Breast Cancer ? |
| 29 | `q401` | Breast Cancer | NIHSeniorHealth | What are the treatments for Breast Cancer ? |
| 30 | `q169` | Prostate Cancer | NIHSeniorHealth | What is (are) Prostate Cancer ? |
| 31 | `q181` | Prostate Cancer | NIHSeniorHealth | Who is at risk for Prostate Cancer? ? |
| 32 | `q396` | Breast Cancer | NIHSeniorHealth | What are the symptoms of Breast Cancer ? |
| 33 | `q405` | Breast Cancer | NIHSeniorHealth | What are the treatments for Breast Cancer ? |
| 34 | `q193` | Prostate Cancer | NIHSeniorHealth | What are the treatments for Prostate Cancer ? |
| 35 | `q517` | Stroke | NIHSeniorHealth | How to prevent Stroke ? |
| 36 | `q1309` | Prostate Cancer | CancerGov | Who is at risk for Prostate Cancer? ? |
| 37 | `q892` | Breast Cancer | CancerGov | How to prevent Breast Cancer ? |
| 38 | `q184` | Prostate Cancer | NIHSeniorHealth | What are the symptoms of Prostate Cancer ? |
| 39 | `q527` | Stroke | NIHSeniorHealth | What is (are) Stroke ? |
| 40 | `q191` | Prostate Cancer | NIHSeniorHealth | What are the treatments for Prostate Cancer ? |
| 41 | `q398` | Breast Cancer | NIHSeniorHealth | Who is at risk for Breast Cancer? ? |
| 42 | `q515` | Stroke | NIHSeniorHealth | Who is at risk for Stroke? ? |
| 43 | `q1161` | Breast Cancer | CancerGov | What are the symptoms of Breast Cancer ? |
| 44 | `q384` | Breast Cancer | NIHSeniorHealth | How to diagnose Breast Cancer ? |
| 45 | `q512` | Stroke | NIHSeniorHealth | What is (are) Stroke ? |
| 46 | `q8469` | Stroke | NHLBI | What are the treatments for Stroke ? |
| 47 | `q178` | Prostate Cancer | NIHSeniorHealth | What is (are) Prostate Cancer ? |
| 48 | `q387` | Breast Cancer | NIHSeniorHealth | what research (or clinical trials) is being done for Breast Cancer ? |
| 49 | `q516` | Stroke | NIHSeniorHealth | What is (are) Stroke ? |
| 50 | `q194` | Prostate Cancer | NIHSeniorHealth | What are the treatments for Prostate Cancer ? |

---

## 3. Detailed Question & Gold Answer Reference

### 01. [q505] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Stroke ?

**Gold Standard Reference Answer**:
> Stroke -- A Serious Event A stroke is serious, just like a heart attack. Each year in the United States, approximately 795,000 people have a stroke. About 610,000 of these are first or new strokes. On average, one American dies from stroke every four minutes. Stroke is the fourth leading cause of death in the United States, and causes more serious long-term disabilities than any other disease. Nearly three-quarters of all strokes occur in people over the age of 65. And the risk of having a stroke more than doubles each decade between the ages of 55 and 85. Stroke occurs in all age groups, in both sexes, and in all races in every country. It can even occur before birth, when the fetus is still in the womb. Learning about stroke can help you act in time to save a relative, neighbor, or friend. And making changes in your lifestyle can help you prevent stroke. What Is Stroke? A stroke is sometimes called a "brain attack." Most often, stroke occurs when blood flow to the brain stops because it is blocked by a clot. When this happens, the brain cells in the immediate area begin to die. Some brain cells die because they stop getting the oxygen and nutrients they need to function. Other brain cells die because they are damaged by sudden bleeding into or around the brain. The brain cells that don't die immediately remain at risk for death. These cells can linger in a compromised or weakened state for several hours. With timely treatment, these cells can be saved. New treatments are available that greatly reduce the damage caused by a stroke. But you need to arrive at the hospital as soon as possible after symptoms start to prevent disability and to greatly improve your chances for recovery. Knowing stroke symptoms, calling 911 immediately, and getting to a hospital as quickly as possible are critical. Ischemic Stroke There are two kinds of stroke. The most common kind of stroke is called ischemic stroke. It accounts for approximately 80 percent of all strokes. An ischemic stroke is caused by a blood clot that blocks or plugs a blood vessel supplying blood to the brain. Blockages that cause ischemic strokes stem from three conditions: - the formation of a clot within a blood vessel of the brain or neck, called thrombosis  - the movement of a clot from another part of the body, such as from the heart to the neck or brain, called an embolism  - a severe narrowing of an artery (stenosis) in or leading to the brain, due to fatty deposits lining the blood vessel walls. the formation of a clot within a blood vessel of the brain or neck, called thrombosis the movement of a clot from another part of the body, such as from the heart to the neck or brain, called an embolism a severe narrowing of an artery (stenosis) in or leading to the brain, due to fatty deposits lining the blood vessel walls. Hemorrhagic Stroke The other kind of stroke is called hemorrhagic stroke. A hemorrhagic stroke is caused by a blood vessel that breaks and bleeds into the brain. One common cause of a hemorrhagic stroke is a bleeding aneurysm. An aneurysm is a weak or thin spot on an artery wall. Over time, these weak spots stretch or balloon out due to high blood pressure. The thin walls of these ballooning aneurysms can rupture and spill blood into the space surrounding brain cells. Artery walls can also break open because they become encrusted, or covered with fatty deposits called plaque, eventually lose their elasticity and become brittle, thin, and prone to cracking. Hypertension, or high blood pressure, increases the risk that a brittle artery wall will give way and release blood into the surrounding brain tissue.

---

### 02. [q394] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: Who is at risk for Breast Cancer? ?

**Gold Standard Reference Answer**:
> Risk factors are conditions or agents that increase a person's chances of getting a disease. Here are the most common risk factors for breast cancer. - Personal and family history. A personal history of breast cancer or breast cancer among one or more of your close relatives, such as a sister, mother, or daughter.  - Estrogen levels in the body. High estrogen levels over a long time may increase the risk of breast cancer. Estrogen levels are highest during the years a woman is menstruating.  - Never being pregnant or having your first child in your mid-30s or later.  - Early menstruation. Having your first menstrual period before age 12.  -  Breast density. Women with very dense breasts have a higher risk of breast cancer than women with low or normal breast density.   -  Combination hormone replacement therapy/Hormone therapy. Estrogen, progestin, or both may be given to replace the estrogen no longer made by the ovaries in postmenopausal women or women who have had their ovaries removed. This is called hormone replacement therapy. (HRT) or hormone therapy (HT). Combination HRT/HT is estrogen combined with progestin. This type of HRT/HT can increase the risk of breast cancer.   - Exposure to radiation. Radiation therapy to the chest for the treatment of cancer can increase the risk of breast cancer, starting 10 years after treatment. Radiation therapy to treat cancer in one breast does not appear to increase the risk of cancer in the other breast.  - Obesity. Obesity increases the risk of breast cancer, especially in postmenopausal women who have not used hormone replacement therapy.   - Alcohol. Drinking alcohol increases the risk of breast cancer. The level of risk rises as the amount of alcohol consumed rises.  - Gaining weight after menopause, especially after natural menopause and/or after age 60.  - Race. White women are at greater risk than black women. However, black women diagnosed with breast cancer are more likely to die of the disease.  - Inherited gene changes. Women who have inherited certain changes in the genes named BRCA1 and BRCA2 have a higher risk of breast cancer, ovarian cancer and maybe colon cancer. The risk of breast cancer caused by inherited gene changes depends on the type of gene mutation, family history of cancer, and other factors. Men who have inherited certain changes in the BRCA2 gene have a higher risk of breast, prostate and pancreatic cancers, and lymphoma.    Five percent to 10 percent of all breast cancers are thought to be inherited.    Personal and family history. A personal history of breast cancer or breast cancer among one or more of your close relatives, such as a sister, mother, or daughter. Estrogen levels in the body. High estrogen levels over a long time may increase the risk of breast cancer. Estrogen levels are highest during the years a woman is menstruating. Never being pregnant or having your first child in your mid-30s or later. Early menstruation. Having your first menstrual period before age 12. Breast density. Women with very dense breasts have a higher risk of breast cancer than women with low or normal breast density. Combination hormone replacement therapy/Hormone therapy. Estrogen, progestin, or both may be given to replace the estrogen no longer made by the ovaries in postmenopausal women or women who have had their ovaries removed. This is called hormone replacement therapy. (HRT) or hormone therapy (HT). Combination HRT/HT is estrogen combined with progestin. This type of HRT/HT can increase the risk of breast cancer. Exposure to radiation. Radiation therapy to the chest for the treatment of cancer can increase the risk of breast cancer, starting 10 years after treatment. Radiation therapy to treat cancer in one breast does not appear to increase the risk of cancer in the other breast. Obesity. Obesity increases the risk of breast cancer, especially in postmenopausal women who have not used hormone replacement therapy. Alcohol. Drinking alcohol increases the risk of breast cancer. The level of risk rises as the amount of alcohol consumed rises. Gaining weight after menopause, especially after natural menopause and/or after age 60. Race. White women are at greater risk than black women. However, black women diagnosed with breast cancer are more likely to die of the disease. Inherited gene changes. Women who have inherited certain changes in the genes named BRCA1 and BRCA2 have a higher risk of breast cancer, ovarian cancer and maybe colon cancer. The risk of breast cancer caused by inherited gene changes depends on the type of gene mutation, family history of cancer, and other factors. Men who have inherited certain changes in the BRCA2 gene have a higher risk of breast, prostate and pancreatic cancers, and lymphoma.    Five percent to 10 percent of all breast cancers are thought to be inherited.   Get information about the BRCA1 and BRCA2 genetic mutations and testing for them. This chart shows what the approximate chances are of a woman getting invasive breast cancer in her lifetime.

---

### 03. [q188] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Prostate Cancer ?

**Gold Standard Reference Answer**:
> Surgery, radiation therapy, and hormonal therapy all have the potential to disrupt sexual desire or performance for a short while or permanently. Discuss your concerns with your health care provider. Several options are available to help you manage sexual problems related to prostate cancer treatment.

---

### 04. [q385] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Breast Cancer ?

**Gold Standard Reference Answer**:
> There are many treatment options for women with breast cancer. The choice of treatment depends on your age and general health, the stage of the cancer, whether or not it has spread beyond the breast, and other factors. If tests show that you have cancer, you should talk with your doctor and make treatment decisions as soon as possible. Studies show that early treatment leads to better outcomes. Working With a Team of Specialists People with cancer often are treated by a team of specialists. The team will keep the primary doctor informed about the patient's progress. The team may include a medical oncologist who is a specialist in cancer treatment, a surgeon, a radiation oncologist who is a specialist in radiation therapy, and others. Before starting treatment, you may want another doctor to review the diagnosis and treatment plan. Some insurance companies require a second opinion. Others may pay for a second opinion if you request it. (Watch the video about this breast cancer survivor's treatment. To enlarge the video, click the brackets in the lower right-hand corner. To reduce the video, press the Escape (Esc) button on your keyboard.) Clinical Trials for Breast Cancer Some breast cancer patients take part in studies of new treatments. These studies, called clinical trials, are designed to find out whether a new treatment is both safe and effective. Often, clinical trials compare a new treatment with a standard one so that doctors can learn which is more effective. Women with breast cancer who are interested in taking part in a clinical trial should talk to their doctor. The U.S. National Institutes of Health, through its National Library of Medicine and other Institutes, maintains a database of clinical trials at ClinicalTrials.gov. See a list of the current clinical trials on breast cancer.

---

### 05. [q1311] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: Who is at risk for Prostate Cancer? ?

**Gold Standard Reference Answer**:
> Avoiding risk factors and increasing protective factors may help prevent cancer.
                    Avoiding cancer risk factors may help prevent certain cancers. Risk factors include smoking, being overweight, and not getting enough exercise. Increasing protective factors such as quitting smoking and exercising may also help prevent some cancers. Talk to your doctor or other health care professional about how you might lower your risk of cancer.
                
                
                    The following risk factors may increase the risk of prostate cancer:
                    Age      Prostate cancer is rare in men younger than 50 years of age. The chance of developing prostate cancer increases as men get older.       Family history of prostate cancer     A man whose father, brother, or son has had prostate cancer has a higher-than-average risk of prostate cancer.       Race     Prostate cancer occurs more often in African-American men than in white men. African-American men with prostate cancer are more likely to die from the disease than white men with prostate cancer.       Hormones    The prostate needs male hormones to work the way it should. The main male sex hormone is testosterone. Testosterone helps the body develop and maintain male sex characteristics.    Testosterone is changed into dihydrotestosterone (DHT) by an enzyme in the body. DHT is important for normal prostate growth but can also cause the prostate to get bigger and may play a part in the development of prostate cancer.       Vitamin E    The Selenium and Vitamin E Cancer Prevention Trial (SELECT) found that vitamin E taken alone increased the risk of prostate cancer. The risk continued even after the men stopped taking vitamin E.       Folic acid    Folate is a kind of vitamin B that occurs naturally in some foods, such as green vegetables, beans and orange juice. Folic acid is a man-made form of folate that is found in vitamin supplements and fortified foods, such as whole-grain breads and cereals. A 10-year study showed that the risk of prostate cancer was increased in men who took 1 milligram (mg) supplements of folic acid. However, the risk of prostate cancer was lower in men who had enough folate in their diets.       Dairy and calcium    A diet high in dairy foods and calcium may cause a small increase in the risk of prostate cancer.
                
                
                    The following protective factors may decrease the risk of prostate cancer:
                    Folate    Folate is a kind of vitamin B that occurs naturally in some foods, such as green vegetables, beans and orange juice. Folic acid is a man-made form of folate that is found in vitamin supplements and fortified foods, such as whole-grain breads and cereals. A 10-year study showed that the risk of prostate cancer was lower in men who had enough folate in their diets. However, the risk of prostate cancer was increased in men who took 1 milligram (mg) supplements of folic acid.       Finasteride and Dutasteride     Finasteride and dutasteride are drugs used to lower the amount of male sex hormones made by the body. These drugs block the enzyme that changes testosterone into dihydrotestosterone (DHT). Higher than normal levels of DHT may play a part in developing prostate cancer. Taking finasteride or dutasteride has been shown to lower the risk for prostate cancer, but it is not known if these drugs lower the risk of death from prostate cancer.    The Prostate Cancer Prevention Trial (PCPT) studied whether the drug finasteride can prevent prostate cancer in healthy men 55 years of age and older. This prevention study showed there were fewer prostate cancers in the group of men that took finasteride compared with the group of men that did not. Also, the men who took finasteride who did have prostate cancer had more aggressive tumors. The number of deaths from prostate cancer was the same in both groups. Men who took finasteride reported more side effects compared with the group of men that did not, including erectile dysfunction, loss of desire for sex, and enlarged breasts.    The Reduction by Dutasteride of Prostate Cancer Events Trial (REDUCE) studied whether the drug dutasteride can prevent prostate cancer in men aged 50 to 75 years at higher risk for the disease. This prevention study showed there were fewer prostate cancers in the group of men who took dutasteride compared with the group of men that did not. The number of less aggressive prostate cancers was lower, but the number of more aggressive prostate cancers was not. Men who took dutasteride reported more side effects than men who did not, including erectile dysfunction, loss of desire for sex, less semen, and gynecomastia (enlarged breasts).
                
                
                    The following have been proven not to affect the risk of prostate cancer, or their effects on prostate cancer risk are not known:
                    Selenium and vitamin E    The Selenium and Vitamin E Cancer Prevention Trial (SELECT) studied whether taking vitamin E and selenium (a mineral) will prevent prostate cancer. The selenium and vitamin E were taken separately or together by healthy men 55 years of age and older (50 years of age and older for African-American men). The study showed that taking selenium alone or selenium and vitamin E together did not decrease the risk of prostate cancer.       Diet    It is not known if decreasing fat or increasing fruits and vegetables in the diet helps decrease the risk of prostate cancer or death from prostate cancer. In the PCPT trial, certain fatty acids increased the risk of high-grade prostate cancer while others decreased the risk of high-grade prostate cancer.       Multivitamins    Regular use of multivitamins has not been proven to increase the risk of early or localized prostate cancer. However, a large study showed an increased risk of advanced prostate cancer among men who took multivitamins more than seven times a week.       Lycopene    Some studies have shown that a diet high in lycopene may be linked to a decreased risk of prostate cancer, but other studies have not. It has not been proven that taking lycopene supplements decreases the risk of prostate cancer.

---

### 06. [q506] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: What are the symptoms of Stroke ?

**Gold Standard Reference Answer**:
> Know the Signs Knowing the warning signs of stroke and controlling stroke's risk factors can lower your risk of death or disability. If you suffer a stroke, you may not realize it at first. The people around you might not know it, either. Your family, friends, or neighbors may think you are unaware or confused. You may not be able to call 911 on your own. That's why everyone should know the signs of stroke and know how to act fast. Warning signs are clues your body sends to tell you that your brain is not receiving enough oxygen. If you observe one or more of the following signs of a stroke or "brain attack," don't wait. Call 911 right away! Common Signs of Stroke These are warning signs of a stroke: - sudden numbness or weakness of the face, arm, or leg, especially on one side of the body  - sudden confusion, trouble speaking or understanding  - sudden trouble seeing in one or both eyes  - sudden trouble walking, dizziness, loss of balance or coordination  - sudden severe headache with no known cause. sudden numbness or weakness of the face, arm, or leg, especially on one side of the body sudden confusion, trouble speaking or understanding sudden trouble seeing in one or both eyes sudden trouble walking, dizziness, loss of balance or coordination sudden severe headache with no known cause. Other danger signs that may occur include double vision, drowsiness, and nausea or vomiting. Don't Ignore "Mini-Strokes" Sometimes the warning signs of stroke may last only a few moments and then disappear. These brief episodes, known as transient ischemic attacks or TIAs, are sometimes called "mini-strokes." Although brief, TIAs identify an underlying serious condition that isn't going away without medical help. Unfortunately, since they clear up, many people ignore them. Don't ignore them. Heeding them can save your life. Why It's Important To Act Fast Stroke is a medical emergency. Every minute counts when someone is having a stroke. The longer blood flow is cut off to the brain, the greater the damage. Immediate treatment can save peoples lives and enhance their chances for successful recovery. Ischemic strokes, the most common type of strokes, can be treated with a drug called t-PA that dissolves blood clots obstructing blood flow to the brain. The window of opportunity to start treating stroke patients is three hours, but to be evaluated and receive treatment, patients need to get to the hospital within 60 minutes. What Should You Do? Don't wait for the symptoms of stroke to improve or worsen. If you believe you are having a stroke, call 911 immediately. Making the decision to call for medical help can make the difference in avoiding a lifelong disability and in greatly improving your chances for recovery. If you observe someone having a stroke  if he or she suddenly loses the ability to speak, or move an arm or leg on one side, or experiences facial paralysis on one side  call 911 immediately.

---

### 07. [q519] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Stroke ?

**Gold Standard Reference Answer**:
> One test that helps doctors judge the severity of a stroke is the standardized NIH Stroke Scale, developed by the National Institute of Neurological Disorders and Stroke at the National Institutes of Health, or NIH. Health care professionals use the NIH Stroke Scale to measure a patient's neurological deficits by asking the patient to answer questions and to perform several physical and mental tests. Other scales include the Glasgow Coma Scale, the Hunt and Hess Scale, the Modified Rankin Scale, and the Barthel Index.

---

### 08. [q1170] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: What is the outlook for Prostate Cancer ?

**Gold Standard Reference Answer**:
> Certain factors affect prognosis (chance of recovery) and treatment options. The prognosis (chance of recovery) and treatment options depend on the following:         - The stage of the cancer (level of PSA, Gleason score, grade of the tumor, how much of the prostate is affected by the cancer, and whether the cancer has spread to other places in the body).    - The patients age.    - Whether the cancer has just been diagnosed or has recurred (come back).        Treatment options also may depend on the following:         - Whether the patient has other health problems.    - The expected side effects of treatment.    - Past treatment for prostate cancer.    - The wishes of the patient.        Most men diagnosed with prostate cancer do not die of it.

---

### 09. [q773] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: How to diagnose Breast Cancer ?

**Gold Standard Reference Answer**:
> Breast exams should be part of prenatal and postnatal care.
		                    To detect breast cancer, pregnant and nursing women should examine their breasts themselves. Women should also receive clinical breast exams during their regular prenatal and postnatal check-ups. Talk to your doctor if you notice any changes in your breasts that you do not expect or that worry you.
		        
		        
		                    Tests that examine the breasts are used to detect (find) and diagnose breast cancer.
		                    The following tests and procedures may be used:         -   Physical exam and history : An exam of the body to check general signs of health, including checking for signs of disease, such as lumps or anything else that seems unusual. A history of the patients health habits and past illnesses and treatments will also be taken.     -  Clinical breast exam (CBE): An exam of the breast by a doctor or other health professional. The doctor will carefully feel the breasts and under the arms for lumps or anything else that seems unusual.     -    MRI (magnetic resonance imaging): A procedure that uses a magnet, radio waves, and a computer to make a series of detailed pictures of both breasts. This procedure is also called nuclear magnetic resonance imaging (NMRI).    -   Ultrasound exam: A procedure in which high-energy sound waves (ultrasound) are bounced off internal tissues or organs and make echoes. The echoes form a picture of body tissues called a sonogram. The picture can be printed to look at later.    -   Mammogram : An x-ray of the breast. A mammogram can be done with little risk to the unborn baby. Mammograms in pregnant women may appear negative even though cancer is present.     -   Blood chemistry studies : A procedure in which a blood sample is checked to measure the amounts of certain substances released into the blood by organs and tissues in the body. An unusual (higher or lower than normal) amount of a substance can be a sign of disease.     -   Biopsy : The removal of cells or tissues so they can be viewed under a microscope by a pathologist to check for signs of cancer. If a lump in the breast is found, a biopsy may be done. There are four types of breast biopsies:               -  Excisional biopsy : The removal of an entire lump of tissue.       -  Incisional biopsy : The removal of part of a lump or a sample of tissue.       -  Core biopsy : The removal of tissue using a wide needle.       -  Fine-needle aspiration (FNA) biopsy : The removal of tissue or fluid, using a thin needle.
		        
		        
		                    If cancer is found, tests are done to study the cancer cells.
		                    Decisions about the best treatment are based on the results of these tests and the age of the unborn baby. The tests give information about:         - How quickly the cancer may grow.    - How likely it is that the cancer will spread to other parts of the body.    - How well certain treatments might work.    - How likely the cancer is to recur (come back).        Tests may include the following:         -   Estrogen and progesterone receptor test : A test to measure the amount of estrogen and progesterone (hormones) receptors in cancer tissue. If there are more estrogen and progesterone receptors than normal, the cancer is called estrogen and/or progesterone receptor positive. This type of breast cancer may grow more quickly. The test results show whether treatment to block estrogen and progesterone given after the baby is born may stop the cancer from growing.    -   Human epidermal growth factor type 2 receptor (HER2/neu) test : A laboratory test to measure how many HER2/neu genes there are and how much HER2/neu protein is made in a sample of tissue. If there are more HER2/neu genes or higher levels of HER2/neu protein than normal, the cancer is called HER2/neu positive. This type of breast cancer may grow more quickly and is more likely to spread to other parts of the body. The cancer may be treated with drugs that target the HER2/neu protein, such as trastuzumab and pertuzumab, after the baby is born.    -  Multigene tests: Tests in which samples of tissue are studied to look at the activity of many genes at the same time. These tests may help predict whether cancer will spread to other parts of the body or recur (come back).               -  Oncotype DX : This test helps predict whether stage I or stage II breast cancer that is estrogen receptor positive and node-negative will spread to other parts of the body. If the risk of the cancer spreading is high, chemotherapy may be given to lower the risk.      -  MammaPrint : This test helps predict whether stage I or stage II breast cancer that is node-negative will spread to other parts of the body. If the risk of the cancer spreading is high, chemotherapy may be given to lower the risk.

---

### 10. [q195] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: Who is at risk for Prostate Cancer? ?

**Gold Standard Reference Answer**:
> Researchers are studying changes in genes that may increase the risk for developing prostate cancer. Some studies are looking at the genes of men who were diagnosed with prostate cancer at a relatively young age, less than 55 years old, and the genes of families who have several members with the disease. Other studies are trying to identify which genes, or arrangements of genes, are most likely to lead to prostate cancer. Much more work is needed, however, before scientists can say exactly how genetic changes relate to prostate cancer. At the moment, no genetic risk has been firmly established.

---

### 11. [q1160] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: Is Breast Cancer inherited ?

**Gold Standard Reference Answer**:
> Breast cancer is sometimes caused by inherited gene mutations (changes). The genes in cells carry the hereditary information that is received from a persons parents. Hereditary breast cancer makes up about 5% to 10% of all breast cancer. Some mutated genes related to breast cancer are more common in certain ethnic groups.   Women who have certain gene mutations, such as a BRCA1 or BRCA2 mutation, have an increased risk of breast cancer. These women also have an increased risk of ovarian cancer, and may have an increased risk of other cancers. Men who have a mutated gene related to breast cancer also have an increased risk of breast cancer. For more information, see the PDQ summary on Male Breast Cancer Treatment.   There are tests that can detect (find) mutated genes. These genetic tests are sometimes done for members of families with a high risk of cancer. See the PDQ summary on Genetics of Breast and Gynecologic Cancers for more information.

---

### 12. [q381] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Breast Cancer ?

**Gold Standard Reference Answer**:
> How Tumors Form The body is made up of many types of cells. Normally, cells grow, divide and produce more cells as needed to keep the body healthy. Sometimes, however, the process goes wrong. Cells become abnormal and form more cells in an uncontrolled way. These extra cells form a mass of tissue, called a growth or tumor. Tumors can be benign, which means not cancerous, or malignant, which means cancerous. Breast cancer occurs when malignant tumors form in the breast tissue. Who Gets Breast Cancer?  Breast cancer is one of the most common cancers in American women. It is most common among women between the ages of 45-85. (Watch the video to learn more about breast cancer survival rates. To enlarge the videos appearing on this page, click the brackets in the lower right-hand corner of the video screen. To reduce the videos, press the Escape (Esc) button on your keyboard.) Men can get breast cancer too, although they account for only 1 percent of all reported cases. Read more about breast cancer in men.  When Breast Cancer Spreads When cancer grows in breast tissue and spreads outside the breast, cancer cells are often found in the lymph nodes under the arm. If the cancer has reached these nodes, it means that cancer cells may have spread, or metastasized, to other parts of the body. When cancer spreads from its original location in the breast to another part of the body such as the brain, it is called metastatic breast cancer, not brain cancer. Doctors sometimes call this "distant" disease.  Learn about different kinds of breast cancer. Breast Cancer is Not Contagious Breast cancer is not contagious. A woman cannot "catch" breast cancer from other women who have the disease. Also, breast cancer is not caused by an injury to the breast. Most women who develop breast cancer do not have any known risk factors or a history of the disease in their families. Treating and Surviving Breast Cancer  Today, more women are surviving breast cancer than ever before. Nearly three million women are breast cancer survivors. (Watch the video to hear a woman discuss surviving breast cancer.) There are several ways to treat breast cancer, but all treatments work best when the disease is found early. As a matter of fact, when it is caught in its earliest stage, 98.5 percent of women with the disease are alive five years later. Every day researchers are working to find new and better ways to detect and treat cancer. Many studies of new approaches for women with breast cancer are under way. With early detection, and prompt and appropriate treatment, the outlook for women with breast cancer can be positive. To learn more about what happens after treatment, see  Surviving Cancer.

---

### 13. [q514] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Stroke ?

**Gold Standard Reference Answer**:
> Transient ischemic attacks, or TIAs, occur when the warning signs of stroke last only a few moments and then disappear. These brief episodes are also sometimes called "mini-strokes." Although brief, they identify an underlying serious condition that isn't going away without medical help. Unfortunately, since they clear up, many people ignore them. Don't ignore them. Heeding them can save your life.

---

### 14. [q173] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Prostate Cancer ?

**Gold Standard Reference Answer**:
> Choosing Treatment There are a number of ways to treat prostate cancer, and the doctor will develop a treatment to fit each man's needs. The choice of treatment mostly depends on the stage of the disease and the grade of the tumor. But doctors also consider a man's age, general health, and his feelings about the treatments and their possible side effects. Treatment for prostate cancer may involve watchful waiting, surgery, radiation therapy, or hormonal therapy. Some men receive a combination of therapies. A cure is the goal for men whose prostate cancer is diagnosed early. Weighing Treatment Options You and your doctor will want to consider both the benefits and possible side effects of each option, especially the effects on sexual activity and urination, and other concerns about quality of life. Surgery, radiation therapy, and hormonal therapy all have the potential to disrupt sexual desire or performance for a short while or permanently. Discuss your concerns with your health care provider. Several options are available to help you manage sexual problems related to prostate cancer treatment. Watchful Waiting The doctor may suggest watchful waiting for some men who have prostate cancer that is found at an early stage and appears to be growing slowly. Also, watchful waiting may be advised for older men or men with other serious medical problems. For these men, the risks and possible side effects of surgery, radiation therapy, or hormonal therapy may outweigh the possible benefits. Doctors monitor these patients with regular check-ups. If symptoms appear or get worse, the doctor may recommend active treatment. Surgery Surgery is used to remove the cancer. It is a common treatment for early stage prostate cancer. The surgeon may remove the entire prostate with a type of surgery called radical prostatectomy or, in some cases, remove only part of it. Sometimes the surgeon will also remove nearby lymph nodes. Side effects of the operation may include lack of sexual function or impotence, or problems holding urine or incontinence. Improvements in surgery now make it possible for some men to keep their sexual function. In some cases, doctors can use a technique known as nerve-sparing surgery. This may save the nerves that control erection. However, men with large tumors or tumors that are very close to the nerves may not be able to have this surgery. Some men with trouble holding urine may regain control within several weeks of surgery. Others continue to have problems that require them to wear a pad. Radiation Therapy Radiation therapy uses high-energy x-rays to kill cancer cells and shrink tumors. Doctors may recommend it instead of surgery, or after surgery, to destroy any cancer cells that may remain in the area. In advanced stages, the doctor may recommend radiation to relieve pain or other symptoms. It may also be used in combination with hormonal therapy. Radiation can cause problems with impotence and bowel function. The radiation may come from a machine, which is external radiation, or from tiny radioactive seeds placed inside or near the tumor, which is internal radiation. Men who receive only the radioactive seeds usually have small tumors. Some men receive both kinds of radiation therapy. For external radiation therapy, patients go to the hospital or clinic -- usually for several weeks. Internal radiation may require patients to stay in the hospital for a short time. Hormonal Therapy Hormonal therapy deprives cancer cells of the male hormones they need to grow and survive. This treatment is often used for prostate cancer that has spread to other parts of the body. Sometimes doctors use hormonal therapy to try to keep the cancer from coming back after surgery or radiation treatment. Side effects can include impotence, hot flashes, loss of sexual desire, and thinning of bones. Some hormone therapies increase the risk of blood clots. Monitoring Treatment Regardless of the type of treatment you receive, you will be closely monitored to see how well the treatment is working. Monitoring may include - a PSA blood test -- usually every 3 months to 1 year.  - bone scan and/or CT scan to see if the cancer has spread.  - a complete blood count to monitor for signs and symptoms of anemia.  - looking for signs or symptoms that the disease might be progressing, such as fatigue, increased pain, or decreased bowel and bladder function. a PSA blood test -- usually every 3 months to 1 year. bone scan and/or CT scan to see if the cancer has spread. a complete blood count to monitor for signs and symptoms of anemia. looking for signs or symptoms that the disease might be progressing, such as fatigue, increased pain, or decreased bowel and bladder function.

---

### 15. [q1162] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: How to diagnose Breast Cancer ?

**Gold Standard Reference Answer**:
> Tests that examine the breasts are used to detect (find) and diagnose breast cancer.
                    Check with your doctor if you notice any changes in your breasts. The following tests and procedures may be used:         -   Physical exam and history : An exam of the body to check general signs of health, including checking for signs of disease, such as lumps or anything else that seems unusual. A history of the patients health habits and past illnesses and treatments will also be taken.     -   Clinical breast exam (CBE): An exam of the breast by a doctor or other health professional. The doctor will carefully feel the breasts and under the arms for lumps or anything else that seems unusual.    -  Mammogram: An x-ray of the breast.     -   Ultrasound exam: A procedure in which high-energy sound waves (ultrasound) are bounced off internal tissues or organs and make echoes. The echoes form a picture of body tissues called a sonogram. The picture can be printed to be looked at later.    -    MRI (magnetic resonance imaging): A procedure that uses a magnet, radio waves, and a computer to make a series of detailed pictures of both breasts. This procedure is also called nuclear magnetic resonance imaging (NMRI).    -   Blood chemistry studies : A procedure in which a blood sample is checked to measure the amounts of certain substances released into the blood by organs and tissues in the body. An unusual (higher or lower than normal) amount of a substance can be a sign of disease.     -   Biopsy : The removal of cells or tissues so they can be viewed under a microscope by a pathologist to check for signs of cancer. If a lump in the breast is found, a biopsy may be done.  There are four types of biopsy used to check for breast cancer:               -  Excisional biopsy : The removal of an entire lump of tissue.       -  Incisional biopsy : The removal of part of a lump or a sample of tissue.       -  Core biopsy : The removal of tissue using a wide needle.       -  Fine-needle aspiration (FNA) biopsy : The removal of tissue or fluid, using a thin needle.
                
                
                    If cancer is found, tests are done to study the cancer cells.
                    Decisions about the best treatment are based on the results of these tests. The tests give information about:         - how quickly the cancer may grow.    - how likely it is that the cancer will spread through the body.    - how well certain treatments might work.    - how likely the cancer is to recur (come back).        Tests include the following:         -   Estrogen and progesterone receptor test : A test to measure the amount of estrogen and progesterone (hormones) receptors in cancer tissue. If there are more estrogen and progesterone receptors than normal, the cancer is called estrogen and/or progesterone receptor positive. This type of breast cancer may grow more quickly. The test results show whether treatment to block estrogen and progesterone may stop the cancer from growing.    -   Human epidermal growth factor type 2 receptor (HER2/neu) test : A laboratory test to measure how many HER2/neu genes there are and how much HER2/neu protein is made in a sample of tissue. If there are more HER2/neu genes or higher levels of HER2/neu protein than normal, the cancer is called HER2/neu positive. This type of breast cancer may grow more quickly and is more likely to spread to other parts of the body. The cancer may be treated with drugs that target the HER2/neu protein, such as trastuzumab and pertuzumab.    -  Multigene tests: Tests in which samples of tissue are studied to look at the activity of many genes at the same time. These tests may help predict whether cancer will spread to other parts of the body or recur (come back). There are many types of multigene tests. The following multigene tests have been studied in clinical trials:               -  Oncotype DX : This test helps predict whether stage I or stage II breast cancer that is estrogen receptor positive and node negative will spread to other parts of the body. If the risk that the cancer will spread is high, chemotherapy may be given to lower the risk.      -  MammaPrint : This test helps predict whether stage I or stage II breast cancer that is node negative will spread to other parts of the body. If the risk that the cancer will spread is high, chemotherapy may be given to lower the risk.                 Based on these tests, breast cancer is described as one of the following types:         -  Hormone receptor positive (estrogen and/or progesterone receptor positive) or hormone receptor negative (estrogen and/or progesterone receptor negative).    - HER2/neu positive or HER2/neu negative.    -  Triple negative (estrogen receptor, progesterone receptor, and HER2/neu negative).         This information helps the doctor decide which treatments will work best for your cancer.

---

### 16. [q1165] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: What are the treatments for Breast Cancer ?

**Gold Standard Reference Answer**:
> Key Points
                    - There are different types of treatment for patients with breast cancer.    - Five types of standard treatment are used:         - Surgery      - Radiation therapy      - Chemotherapy      - Hormone therapy      - Targeted therapy        - New types of treatment are being tested in clinical trials.          - High-dose chemotherapy with stem cell transplant        - Treatment for breast cancer may cause side effects.    - Patients may want to think about taking part in a clinical trial.    - Patients can enter clinical trials before, during, or after starting their cancer treatment.    - Follow-up tests may be needed.
                
                
                    There are different types of treatment for patients with breast cancer.
                    Different types of treatment are available for patients with breast cancer. Some treatments are standard (the currently used treatment), and some are being tested in clinical trials. A treatment clinical trial is a research study meant to help improve current treatments or obtain information on new treatments for patients with cancer. When clinical trials show that a new treatment is better than the standard treatment, the new treatment may become the standard treatment. Patients may want to think about taking part in a clinical trial. Some clinical trials are open only to patients who have not started treatment.
                
                
                    Five types of standard treatment are used:
                    Surgery     Most patients with breast cancer have surgery to remove the cancer.     Sentinel lymph node biopsy is the removal of the sentinel lymph node during surgery. The sentinel lymph node is the first lymph node to receive lymphatic drainage from a tumor. It is the first lymph node where the cancer is likely to spread. A radioactive substance and/or blue dye is injected near the tumor. The substance or dye flows through the lymph ducts to the lymph nodes. The first lymph node to receive the substance or dye is removed. A pathologist views the tissue under a microscope to look for cancer cells. After the sentinel lymph node biopsy, the surgeon removes the tumor using breast-conserving surgery or mastectomy. If cancer cells were not found in the sentinel lymph node, it may not be necessary to remove more lymph nodes. If cancer cells were found, more lymph nodes will be removed through a separate incision. This is called a lymph node dissection.    Types of surgery include the following:            - Breast-conserving surgery is an operation to remove the cancer and some normal tissue around it, but not the breast itself. Part of the chest wall lining may also be removed if the cancer is near it. This type of surgery may also be called lumpectomy, partial mastectomy, segmental mastectomy, quadrantectomy, or breast-sparing surgery.     -  Total mastectomy: Surgery to remove the whole breast that has cancer. This procedure is also called a simple mastectomy. Some of the lymph nodes under the arm may be removed and checked for cancer. This may be done at the same time as the breast surgery or after. This is done through a separate incision.      -  Modified radical mastectomy: Surgery to remove the whole breast that has cancer, many of the lymph nodes under the arm, the lining over the chest muscles, and sometimes, part of the chest wall muscles.             Chemotherapy may be given before surgery to remove the tumor. When given before surgery, chemotherapy will shrink the tumor and reduce the amount of tissue that needs to be removed during surgery. Treatment given before surgery is called preoperative therapy or neoadjuvant therapy.    Even if the doctor removes all the cancer that can be seen at the time of the surgery, some patients may be given radiation therapy, chemotherapy, or hormone therapy after surgery, to kill any cancer cells that are left. Treatment given after the surgery, to lower the risk that the cancer will come back, is called postoperative therapy or adjuvant therapy.     If a patient is going to have a mastectomy, breast reconstruction (surgery to rebuild a breasts shape after a mastectomy) may be considered. Breast reconstruction may be done at the time of the mastectomy or at some time after. The reconstructed breast may be made with the patients own (nonbreast) tissue or by using implants filled with saline or silicone gel. Before the decision to get an implant is made, patients can call the Food and Drug Administration's (FDA) Center for Devices and Radiologic Health at 1-888-INFO-FDA (1-888-463-6332) or visit the FDA website for more information on breast implants.        Radiation therapy     Radiation therapy is a cancer treatment that uses high-energy x-rays or other types of radiation to kill cancer cells or keep them from growing. There are two types of radiation therapy:            -  External radiation therapy uses a machine outside the body to send radiation toward the cancer.     -  Internal radiation therapy uses a radioactive substance sealed in needles, seeds, wires, or catheters that are placed directly into or near the cancer.           The way the radiation therapy is given depends on the type and stage of the cancer being treated. External radiation therapy is used to treat breast cancer. Internal radiation therapy with strontium-89 (a radionuclide) is used to relieve bone pain caused by breast cancer that has spread to the bones. Strontium-89 is injected into a vein and travels to the surface of the bones. Radiation is released and kills cancer cells in the bones.       Chemotherapy     Chemotherapy is a cancer treatment that uses drugs to stop the growth of cancer cells, either by killing the cells or by stopping them from dividing. When chemotherapy is taken by mouth or injected into a vein or muscle, the drugs enter the bloodstream and can reach cancer cells throughout the body (systemic chemotherapy). When chemotherapy is placed directly into the cerebrospinal fluid, an organ, or a body cavity such as the abdomen, the drugs mainly affect cancer cells in those areas (regional chemotherapy).     The way the chemotherapy is given depends on the type and stage of the cancer being treated. Systemic chemotherapy is used in the treatment of breast cancer.    See Drugs Approved for Breast Cancer for more information.       Hormone therapy      Hormone therapy is a cancer treatment that removes hormones or blocks their action and stops cancer cells from growing. Hormones are substances made by glands in the body and circulated in the bloodstream. Some hormones can cause certain cancers to grow. If tests show that the cancer cells have places where hormones can attach (receptors), drugs, surgery, or radiation therapy is used to reduce the production of hormones or block them from working. The hormone estrogen, which makes some breast cancers grow, is made mainly by the ovaries. Treatment to stop the ovaries from making estrogen is called ovarian ablation.     Hormone therapy with tamoxifen is often given to patients with early localized breast cancer that can be removed by surgery and those with metastatic breast cancer (cancer that has spread to other parts of the body). Hormone therapy with tamoxifen or estrogens can act on cells all over the body and may increase the chance of developing endometrial cancer. Women taking tamoxifen should have a pelvic exam every year to look for any signs of cancer. Any vaginal bleeding, other than menstrual bleeding, should be reported to a doctor as soon as possible.    Hormone therapy with a luteinizing hormone-releasing hormone (LHRH) agonist is given to some premenopausal women who have just been diagnosed with hormone receptor positive breast cancer. LHRH agonists decrease the body's estrogen and progesterone.     Hormone therapy with an aromatase inhibitor is given to some postmenopausal women who have hormone receptor positive breast cancer. Aromatase inhibitors decrease the body's estrogen by blocking an enzyme called aromatase from turning androgen into estrogen. Anastrozole, letrozole, and exemestane are types of aromatase inhibitors.    For the treatment of early localized breast cancer that can be removed by surgery, certain aromatase inhibitors may be used as adjuvant therapy instead of tamoxifen or after 2 to 3 years of tamoxifen use. For the treatment of metastatic breast cancer, aromatase inhibitors are being tested in clinical trials to compare them to hormone therapy with tamoxifen.    Other types of hormone therapy include megestrol acetate or anti-estrogen therapy such as fulvestrant.    See Drugs Approved for Breast Cancer for more information.       Targeted therapy     Targeted therapy is a type of treatment that uses drugs or other substances to identify and attack specific cancer cells without harming normal cells. Monoclonal antibodies, tyrosine kinase inhibitors, cyclin-dependent kinase inhibitors, mammalian target of rapamycin (mTOR) inhibitors, and PARP inhibitors are types of targeted therapies used in the treatment of breast cancer.    Monoclonal antibody therapy is a cancer treatment that uses antibodies made in the laboratory, from a single type of immune system cell. These antibodies can identify substances on cancer cells or normal substances that may help cancer cells grow. The antibodies attach to the substances and kill the cancer cells, block their growth, or keep them from spreading. Monoclonal antibodies are given by infusion. They may be used alone or to carry drugs, toxins, or radioactive material directly to cancer cells. Monoclonal antibodies may be used in combination with chemotherapy as adjuvant therapy.    Types of monoclonal antibody therapy include the following:            -  Trastuzumab is a monoclonal antibody that blocks the effects of the growth factor protein HER2, which sends growth signals to breast cancer cells. It may be used with other therapies to treat HER2 positive breast cancer.      -  Pertuzumab is a monoclonal antibody that may be combined with trastuzumab and chemotherapy to treat breast cancer. It may be used to treat certain patients with HER2 positive breast cancer that has metastasized (spread to other parts of the body). It may also be used as neoadjuvant therapy in certain patients with early stage HER2 positive breast cancer.     -  Ado-trastuzumab emtansine is a monoclonal antibody linked to an anticancer drug. This is called an antibody-drug conjugate. It is used to treat HER2 positive breast cancer that has spread to other parts of the body or recurred (come back).            Tyrosine kinase inhibitors are targeted therapy drugs that block signals needed for tumors to grow. Tyrosine kinase inhibitors may be used with other anticancer drugs as adjuvant therapy. Tyrosine kinase inhibitors include the following:            -  Lapatinib is a tyrosine kinase inhibitor that blocks the effects of the HER2 protein and other proteins inside tumor cells. It may be used with other drugs to treat patients with HER2 positive breast cancer that has progressed after treatment with trastuzumab.           Cyclin-dependent kinase inhibitors are targeted therapy drugs that block proteins called cyclin-dependent kinases, which cause the growth of cancer cells. Cyclin-dependent kinase inhibitors include the following:            -  Palbociclib is a cyclin-dependent kinase inhibitor used with the drug letrozole to treat breast cancer that is estrogen receptor positive and HER2 negative and has spread to other parts of the body. It is used in postmenopausal women whose cancer has not been treated with hormone therapy. Palbociclib may also be used with fulvestrant in women whose disease has gotten worse after treatment with hormone therapy.      -  Ribociclib is a cyclin-dependent kinase inhibitor used with letrozole to treat breast cancer that is hormone receptor positive and HER2 negative and has come back or spread to other parts of the body. It is used in postmenopausal women whose cancer has not been treated with hormone therapy.            Mammalian target of rapamycin (mTOR) inhibitors block a protein called mTOR, which may keep cancer cells from growing and prevent the growth of new blood vessels that tumors need to grow. mTOR inhibitors include the following:            -  Everolimus is an mTOR inhibitor used in postmenopausal women with advanced hormone receptor positive breast cancer that is also HER2 negative and has not gotten better with other treatment.            PARP inhibitors are a type of targeted therapy that block DNA repair and may cause cancer cells to die. PARP inhibitor therapy is being studied for the treatment of patients with triple negative breast cancer or tumors with  BRCA1  or  BRCA2  mutations.    See Drugs Approved for Breast Cancer for more information.
                
                
                    New types of treatment are being tested in clinical trials.
                    This summary section describes treatments that are being studied in clinical trials. It may not mention every new treatment being studied. Information about clinical trials is available from the NCI website.     High-dose chemotherapy with stem cell transplant     High-dose chemotherapy with stem cell transplant is a way of giving high doses of chemotherapy and replacing blood -forming cells destroyed by the cancer treatment. Stem cells (immature blood cells) are removed from the blood or bone marrow of the patient or a donor and are frozen and stored. After the chemotherapy is completed, the stored stem cells are thawed and given back to the patient through an infusion. These reinfused stem cells grow into (and restore) the bodys blood cells.    Studies have shown that high-dose chemotherapy followed by stem cell transplant does not work better than standard chemotherapy in the treatment of breast cancer. Doctors have decided that, for now, high-dose chemotherapy should be tested only in clinical trials. Before taking part in such a trial, women should talk with their doctors about the serious side effects, including death, that may be caused by high-dose chemotherapy.
                
                
                    Treatment for breast cancer may cause side effects.
                    For information about side effects that begin during treatment for cancer, see our Side Effects page.   Some treatments for breast cancer may cause side effects that continue or appear months or years after treatment has ended. These are called late effects.   Late effects of radiation therapy are not common, but may include:         -  Inflammation of the lung after radiation therapy to the breast, especially when chemotherapy is given at the same time.     - Arm lymphedema, especially when radiation therapy is given after lymph node dissection.     - In women younger than 45 years who receive radiation therapy to the chest wall after mastectomy, there may be a higher risk of developing breast cancer in the other breast.        Late effects of chemotherapy depend on the drugs used, but may include:         -  Heart failure.    -  Blood clots.    -  Premature menopause.    -  Second cancer, such as leukemia.        Late effects of targeted therapy with trastuzumab, lapatinib, or pertuzumab may include:         - Heart problems such as heart failure.
                
                
                    Patients may want to think about taking part in a clinical trial.
                    For some patients, taking part in a clinical trial may be the best treatment choice. Clinical trials are part of the cancer research process. Clinical trials are done to find out if new cancer treatments are safe and effective or better than the standard treatment.   Many of today's standard treatments for cancer are based on earlier clinical trials. Patients who take part in a clinical trial may receive the standard treatment or be among the first to receive a new treatment.   Patients who take part in clinical trials also help improve the way cancer will be treated in the future. Even when clinical trials do not lead to effective new treatments, they often answer important questions and help move research forward.
                
                
                    Patients can enter clinical trials before, during, or after starting their cancer treatment.
                    Some clinical trials only include patients who have not yet received treatment. Other trials test treatments for patients whose cancer has not gotten better. There are also clinical trials that test new ways to stop cancer from recurring (coming back) or reduce the side effects of cancer treatment.   Clinical trials are taking place in many parts of the country. See the Treatment Options section that follows for links to current treatment clinical trials. These have been retrieved from NCI's listing of clinical trials.
                
                
                    Follow-up tests may be needed.
                    Some of the tests that were done to diagnose the cancer or to find out the stage of the cancer may be repeated. Some tests will be repeated in order to see how well the treatment is working. Decisions about whether to continue, change, or stop treatment may be based on the results of these tests.   Some of the tests will continue to be done from time to time after treatment has ended. The results of these tests can show if your condition has changed or if the cancer has recurred (come back). These tests are sometimes called follow-up tests or check-ups.
                
		        
		            Treatment Options for Breast Cancer
		            
		                
		                    Early, Localized, or Operable Breast Cancer
		                    Treatment of early, localized, or operable breast cancer may include the following:       Surgery             -  Breast-conserving surgery and sentinel lymph node biopsy. If cancer is found in the lymph nodes, a lymph node dissection may be done.     -  Modified radical mastectomy. Breast reconstruction surgery may also be done.                Postoperative radiation therapy     For women who had breast-conserving surgery, radiation therapy is given to the whole breast to lessen the chance the cancer will come back. Radiation therapy may also be given to lymph nodes in the area.    For women who had a modified radical mastectomy, radiation therapy may be given to lessen the chance the cancer will come back if any of the following are true:            - Cancer was found in 4 or more lymph nodes.     - Cancer had spread to tissue around the lymph nodes.     - The tumor was large.     - There is tumor close to or remaining in the tissue near the edges of where the tumor was removed.                Postoperative systemic therapy      Systemic therapy is the use of drugs that can enter the bloodstream and reach cancer cells throughout the body. Postoperative systemic therapy is given to lessen the chance the cancer will come back after surgery to remove the tumor.    Postoperative systemic therapy is given depending on whether:            - The tumor is hormone receptor negative or positive.     - The tumor is HER2/neu negative or positive.     - The tumor is hormone receptor negative and HER2/neu negative (triple negative).     - The size of the tumor.           In premenopausal women with hormone receptor positive tumors, no more treatment may be needed or postoperative therapy may include:            -  Tamoxifen therapy with or without chemotherapy.     - Tamoxifen therapy and treatment to stop or lessen how much estrogen is made by the ovaries. Drug therapy, surgery to remove the ovaries, or radiation therapy to the ovaries may be used.     -  Aromatase inhibitor therapy and treatment to stop or lessen how much estrogen is made by the ovaries. Drug therapy, surgery to remove the ovaries, or radiation therapy to the ovaries may be used.           In postmenopausal women with hormone receptor positive tumors, no more treatment may be needed or postoperative therapy may include:            - Aromatase inhibitor therapy with or without chemotherapy.     - Tamoxifen followed by aromatase inhibitor therapy, with or without chemotherapy.           In women with hormone receptor negative tumors, no more treatment may be needed or postoperative therapy may include:            - Chemotherapy.           In women with HER2/neu negative tumors, postoperative therapy may include:            - Chemotherapy.           In women with small, HER2/neu positive tumors, and no cancer in the lymph nodes, no more treatment may be needed. If there is cancer in the lymph nodes, or the tumor is large, postoperative therapy may include:            - Chemotherapy and targeted therapy (trastuzumab).     -  Hormone therapy, such as tamoxifen or aromatase inhibitor therapy, for tumors that are also hormone receptor positive.           In women with small, hormone receptor negative and HER2/neu negative tumors (triple negative) and no cancer in the lymph nodes, no more treatment may be needed. If there is cancer in the lymph nodes or the tumor is large, postoperative therapy may include:            - Chemotherapy.     - Radiation therapy.     - A clinical trial of a new chemotherapy regimen.     - A clinical trial of PARP inhibitor therapy.                Preoperative systemic therapy     Systemic therapy is the use of drugs that can enter the bloodstream and reach cancer cells throughout the body. Preoperative systemic therapy is given to shrink the tumor before surgery.    In postmenopausal women with hormone receptor positive tumors, preoperative therapy may include:            - Chemotherapy.     - Hormone therapy, such as tamoxifen or aromatase inhibitor therapy, for women who cannot have chemotherapy.           In premenopausal women with hormone receptor positive tumors, preoperative therapy may include:            - A clinical trial of hormone therapy, such as tamoxifen or aromatase inhibitor therapy.           In women with HER2/neu positive tumors, preoperative therapy may include:            - Chemotherapy and targeted therapy (trastuzumab).     - Targeted therapy (pertuzumab).           In women with HER2/neu negative tumors or triple negative tumors, preoperative therapy may include:            - Chemotherapy.            Check the list of NCI-supported cancer clinical trials that are now accepting patients with stage I breast cancer, stage II breast cancer, stage IIIA breast cancer and stage IIIC breast cancer. For more specific results, refine the search by using other search features, such as the location of the trial, the type of treatment, or the name of the drug. Talk with your doctor about clinical trials that may be right for you. General information about clinical trials is available from the NCI website.
		                
		                
		                    Locally Advanced or Inflammatory Breast Cancer
		                    Treatment of locally advanced or inflammatory breast cancer is a combination of therapies that may include the following:         -  Surgery (breast-conserving surgery or total mastectomy) with lymph node dissection.    -  Chemotherapy before and/or after surgery.    -  Radiation therapy after surgery.    -  Hormone therapy after surgery for tumors that are estrogen receptor positive or estrogen receptor unknown.    -  Clinical trials testing new anticancer drugs, new drug combinations, and new ways of giving treatment.         Check the list of NCI-supported cancer clinical trials that are now accepting patients with stage IIIB breast cancer, stage IIIC breast cancer, stage IV breast cancer and inflammatory breast cancer. For more specific results, refine the search by using other search features, such as the location of the trial, the type of treatment, or the name of the drug. Talk with your doctor about clinical trials that may be right for you. General information about clinical trials is available from the NCI website.
		                
		                
		                    Locoregional Recurrent Breast Cancer
		                    Treatment of locoregional recurrent breast cancer (cancer that has come back after treatment in the breast, in the chest wall, or in nearby lymph nodes), may include the following:         -  Chemotherapy.    -  Hormone therapy for tumors that are hormone receptor positive.    -  Radiation therapy.    -  Surgery.    -  Targeted therapy (trastuzumab).     - A clinical trial of a new treatment.        See the Metastatic Breast Cancer section for information about treatment options for breast cancer that has spread to parts of the body outside the breast, chest wall, or nearby lymph nodes.   Check the list of NCI-supported cancer clinical trials that are now accepting patients with recurrent breast cancer. For more specific results, refine the search by using other search features, such as the location of the trial, the type of treatment, or the name of the drug. Talk with your doctor about clinical trials that may be right for you. General information about clinical trials is available from the NCI website.
		                
		                
		                    Metastatic Breast Cancer
		                    Treatment options for metastatic breast cancer (cancer that has spread to distant parts of the body) may include the following:       Hormone therapy     In postmenopausal women who have just been diagnosed with metastatic breast cancer that is hormone receptor positive or if the hormone receptor status is not known, treatment may include:            -  Tamoxifen therapy.     -  Aromatase inhibitor therapy (anastrozole, letrozole, or exemestane). Sometimes cyclin-dependent kinase inhibitor therapy (palbociclib) is also given.           In premenopausal women who have just been diagnosed with metastatic breast cancer that is hormone receptor positive, treatment may include:             - Tamoxifen, an LHRH agonist, or both.           In women whose tumors are hormone receptor positive or hormone receptor unknown, with spread to the bone or soft tissue only, and who have been treated with tamoxifen, treatment may include:             - Aromatase inhibitor therapy.     - Other hormone therapy such as megestrol acetate, estrogen or androgen therapy, or anti-estrogen therapy such as fulvestrant.                Targeted therapy     In women with metastatic breast cancer that is hormone receptor positive and has not responded to other treatments, options may include targeted therapy such as:            -  Trastuzumab, lapatinib, pertuzumab, or mTOR inhibitors.     -  Antibody-drug conjugate therapy with ado-trastuzumab emtansine.     - Cyclin-dependent kinase inhibitor therapy (palbociclib) combined with letrozole.           In women with metastatic breast cancer that is HER2/neu positive, treatment may include:             - Targeted therapy such as trastuzumab, pertuzumab, ado-trastuzumab emtansine, or lapatinib.                Chemotherapy     In women with metastatic breast cancer that is hormone receptor negative, has not responded to hormone therapy, has spread to other organs or has caused symptoms, treatment may include:            -  Chemotherapy with one or more drugs.                Surgery             -  Total mastectomy for women with open or painful breast lesions. Radiation therapy may be given after surgery.     - Surgery to remove cancer that has spread to the brain or spine. Radiation therapy may be given after surgery.     - Surgery to remove cancer that has spread to the lung.     - Surgery to repair or help support weak or broken bones. Radiation therapy may be given after surgery.     - Surgery to remove fluid that has collected around the lungs or heart.                Radiation therapy             - Radiation therapy to the bones, brain, spinal cord, breast, or chest wall to relieve symptoms and improve quality of life.     -  Strontium-89 (a radionuclide) to relieve pain from cancer that has spread to bones throughout the body.                Other treatment options     Other treatment options for metastatic breast cancer include:            - Drug therapy with bisphosphonates or denosumab to reduce bone disease and pain when cancer has spread to the bone. (See the PDQ summary on Cancer Pain for more information about bisphosphonates.)     - A clinical trial of high-dose chemotherapy with stem cell transplant.     - Clinical trials testing new anticancer drugs, new drug combinations, and new ways of giving treatment.            Check the list of NCI-supported cancer clinical trials that are now accepting patients with metastatic cancer. For more specific results, refine the search by using other search features, such as the location of the trial, the type of treatment, or the name of the drug. Talk with your doctor about clinical trials that may be right for you. General information about clinical trials is available from the NCI website.

---

### 17. [q390] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Breast Cancer ?

**Gold Standard Reference Answer**:
> When cancer spreads from its original location in the breast to another part of the body such as the brain, it is called metastatic breast cancer, not brain cancer. Doctors sometimes call this "distant" disease.

---

### 18. [q772] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: What are the symptoms of Breast Cancer ?

**Gold Standard Reference Answer**:
> Signs of breast cancer include a lump or change in the breast.
                    These and other signs may be caused by breast cancer or by other conditions. Check with your doctor if you have any of the following:         - A lump or thickening in or near the breast or in the underarm area.    -  A change in the size or shape of the breast.    -  A dimple or puckering in the skin of the breast.    -  A nipple turned inward into the breast.    - Fluid, other than breast milk, from the nipple, especially if it's bloody.    - Scaly, red, or swollen skin on the breast, nipple, or areola (the dark area of skin around the nipple).    - Dimples in the breast that look like the skin of an orange, called peau dorange.
                
                
                    It may be difficult to detect (find) breast cancer early in pregnant or nursing women.
                    The breasts usually get larger, tender, or lumpy in women who are pregnant, nursing, or have just given birth. This occurs because of normal hormone changes that take place during pregnancy. These changes can make small lumps difficult to detect. The breasts may also become denser. It is more difficult to detect breast cancer in women with dense breasts using mammography. Because these breast changes can delay diagnosis, breast cancer is often found at a later stage in these women.

---

### 19. [q1158] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: Who is at risk for Breast Cancer? ?

**Gold Standard Reference Answer**:
> A family history of breast cancer and other factors increase the risk of breast cancer.
                    Anything that increases your chance of getting a disease is called a risk factor. Having a risk factor does not mean that you will get cancer; not having risk factors doesn't mean that you will not get cancer. Talk to your doctor if you think you may be at risk for breast cancer.    Risk factors for breast cancer include the following:            - A personal history of invasive breast cancer, ductal carcinoma in situ (DCIS), or lobular carcinoma in situ (LCIS).     - A personal history of benign (noncancer) breast disease.     - A family history of breast cancer in a first-degree relative (mother, daughter, or sister).     - Inherited changes in the  BRCA1  or  BRCA2  genes or in other genes that increase the risk of breast cancer.     - Breast tissue that is dense on a mammogram.     -  Exposure of breast tissue to estrogen made by the body. This may be caused by:                  -  Menstruating at an early age.       -  Older age at first birth or never having given birth.       - Starting menopause at a later age.                - Taking hormones such as estrogen combined with progestin for symptoms of menopause.     - Treatment with radiation therapy to the breast/chest.     - Drinking alcohol.     -  Obesity.           Older age is the main risk factor for most cancers. The chance of getting cancer increases as you get older.      NCI's Breast Cancer Risk Assessment Tool uses a woman's risk factors to estimate her risk for breast cancer during the next five years and up to age 90. This online tool is meant to be used by a health care provider. For more information on breast cancer risk, call 1-800-4-CANCER.

---

### 20. [q776] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: What are the treatments for Breast Cancer ?

**Gold Standard Reference Answer**:
> Key Points
                    - Treatment options for pregnant women depend on the stage of the disease and the age of the unborn baby.     - Three types of standard treatment are used:         - Surgery      - Radiation therapy      - Chemotherapy         - Ending the pregnancy does not seem to improve the mothers chance of survival.    - Treatment for breast cancer may cause side effects.
                
                
                    Treatment options for pregnant women depend on the stage of the disease and the age of the unborn baby.
                    
                
                
                    Three types of standard treatment are used:
                    Surgery     Most pregnant women with breast cancer have surgery to remove the breast. Some of the  lymph nodes under the arm may be removed and checked under a microscope for signs of cancer.    Types of surgery to remove the cancer include:            -  Modified radical mastectomy: Surgery to remove the whole breast that has cancer, many of the lymph nodes under the arm, the lining over the chest muscles, and sometimes, part of the chest wall muscles. This type of surgery is most common in pregnant women.     -  Breast-conserving surgery: Surgery to remove the cancer and some normal tissue around it, but not the breast itself. Part of the chest wall lining may also be removed if the cancer is near it. This type of surgery may also be called lumpectomy, partial mastectomy, segmental mastectomy, quadrantectomy, or breast-sparing surgery.           Even if the doctor removes all of the cancer that can be seen at the time of surgery, the patient may be given radiation therapy or chemotherapy after surgery to try to kill any cancer cells that may be left. For pregnant women with early-stage breast cancer, radiation therapy and hormone therapy are given after the baby is born. Treatment given after surgery, to lower the risk that the cancer will come back, is called adjuvant therapy.       Radiation therapy     Radiation therapy is a cancer treatment that uses high-energy x-rays or other types of radiation to kill cancer cells or keep them from growing. There are two types of radiation therapy:            -  External radiation therapy uses a machine outside the body to send radiation toward the cancer.     -  Internal radiation therapy uses a radioactive substance sealed in needles, seeds, wires, or catheters that are placed directly into or near the cancer.           The way the radiation therapy is given depends on the type and stage of the cancer being treated.    External radiation therapy is not given to pregnant women with early stage (stage I or II) breast cancer because it can harm the unborn baby. For women with late stage (stage III or IV) breast cancer, radiation therapy is not given during the first 3 months of pregnancy and is delayed until after the baby is born, if possible.       Chemotherapy     Chemotherapy is a cancer treatment that uses drugs to stop the growth of cancer cells, either by killing the cells or by stopping the cells from dividing. When chemotherapy is taken by mouth or injected into a vein or muscle, the drugs enter the bloodstream and can reach cancer cells throughout the body (systemic chemotherapy). When chemotherapy is placed directly into the cerebrospinal fluid, an organ, or a body cavity such as the abdomen, the drugs mainly affect cancer cells in those areas (regional chemotherapy). The way the chemotherapy is given depends on the type and stage of the cancer being treated.    Chemotherapy is usually not given during the first 3 months of pregnancy. Chemotherapy given after this time does not usually harm the unborn baby but may cause early labor and low birth weight.    See Drugs Approved for Breast Cancer for more information.
                
                
                    Ending the pregnancy does not seem to improve the mothers chance of survival.
                    Because ending the pregnancy is not likely to improve the mothers chance of survival, it is not usually a treatment option.
                
                
                    Treatment for breast cancer may cause side effects.
                    For information about side effects caused by treatment for cancer, see our Side Effects page.
                
		        
		            Treatment Options by Stage
		            
		                
		                    Early Stage Breast Cancer (Stage I and Stage II)
		                    Treatment of early-stage breast cancer (stage I and stage II) may include the following:          -  Modified radical mastectomy.    -  Breast-conserving surgery followed by radiation therapy. In pregnant women, radiation therapy is delayed until after the baby is born.    - Modified radical mastectomy or breast-conserving surgery during pregnancy followed by chemotherapy after the first 3 months of pregnancy.
		                
		                
		                    Late Stage Breast Cancer (Stage III and Stage IV)
		                    Treatment of late-stage breast cancer (stage III and stage IV) may include the following:         -  Radiation therapy.    -  Chemotherapy.        Radiation therapy and chemotherapy should not be given during the first 3 months of pregnancy.

---

### 21. [q187] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Prostate Cancer ?

**Gold Standard Reference Answer**:
> There are a number of ways to treat prostate cancer, and the doctor will develop a treatment to fit each man's needs. The choice of treatment mostly depends on the stage of the disease and the grade of the tumor. But doctors also consider a man's age, general health, and his feelings about the treatments and their possible side effects. Treatment for prostate cancer may involve watchful waiting, surgery, radiation therapy, or hormonal therapy. Some men receive a combination of therapies. A cure is probable for men whose prostate cancer is diagnosed early.

---

### 22. [q179] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What causes Prostate Cancer ?

**Gold Standard Reference Answer**:
> Scientists don't know exactly what causes prostate cancer. They cannot explain why one man gets prostate cancer and another does not. However, they have been able to identify some risk factors that are associated with the disease. A risk factor is anything that increases your chances of getting a disease.

---

### 23. [q8466] Stroke
- **Focus Area**: Stroke
- **Data Source**: NHLBI
- **Question**: Who is at risk for Stroke? ?

**Gold Standard Reference Answer**:
> Certain traits, conditions, and habits can raise your risk of having a stroke or transient ischemic attack (TIA). These traits, conditions, and habits are known as risk factors.
                
The more risk factors you have, the more likely you are to have a stroke. You can treat or control some risk factors, such as high blood pressure and smoking. Other risk factors, such as age and gender, you cant control.
                
The major risk factors for stroke include:
                
High blood pressure. High blood pressure is the main risk factor for stroke. Blood pressure is considered high if it stays at or above 140/90 millimeters of mercury (mmHg) over time. If you have diabetes or chronic kidney disease, high blood pressure is defined as 130/80 mmHg or higher.
                
Diabetes. Diabetes is a disease in which the blood sugar level is high because the body doesnt make enough insulin or doesnt use its insulin properly. Insulin is a hormone that helps move blood sugar into cells where its used for energy.
                
Heart diseases.Coronary heart disease,cardiomyopathy,heart failure, andatrial fibrillationcan cause blood clots that can lead to a stroke.
                
Smoking. Smoking can damage blood vessels and raise blood pressure. Smoking also may reduce the amount of oxygen that reaches your bodys tissues. Exposure to secondhand smoke also can damage the blood vessels.
                
Age and gender. Your risk of stroke increases as you get older. At younger ages, men are more likely than women to have strokes. However, women are more likely to die from strokes. Women who take birth control pills also are at slightly higher risk of stroke.
                
Race and ethnicity. Strokes occur more often in African American, Alaska Native, and American Indian adults than in white, Hispanic, or Asian American adults.
                
Personal or family history of stroke or TIA. If youve had a stroke, youre at higher risk for another one. Your risk of having a repeat stroke is the highest right after a stroke. A TIA also increases your risk of having a stroke, as does having a family history of stroke.
                
Brainaneurysmsor arteriovenous malformations (AVMs). Aneurysms are balloon-like bulges in an artery that can stretch and burst. AVMs are tangles of faulty arteries and veins that can rupture (break open) within the brain. AVMs may be present at birth, but often arent diagnosed until they rupture.
                
Other risk factors for stroke, many of which of you can control, include:
                
Alcohol and illegal drug use, including cocaine, amphetamines, and other drugs
                
Certain medical conditions, such as sickle cell disease, vasculitis (inflammation of the blood vessels), and bleeding disorders
                
Lack of physical activity
                
Overweight and Obesity
                
Stress and depression
                
Unhealthy cholesterol levels
                
Unhealthy diet
                
Use of nonsteroidal anti-inflammatory drugs (NSAIDs), but not aspirin, may increase the risk of heart attack or stroke, particularly in patients who have had a heart attack or cardiac bypass surgery. The risk may increase the longer NSAIDs are used. Common NSAIDs include ibuprofen and naproxen.
                
Following a healthy lifestyle can lower the risk of stroke. Some people also may need to take medicines to lower their risk. Sometimes strokes can occur in people who dont have any known risk factors.

---

### 24. [q180] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: Who is at risk for Prostate Cancer? ?

**Gold Standard Reference Answer**:
> Age is the most important risk factor for prostate cancer. The disease is extremely rare in men under age 40, but the risk increases greatly with age. More than 60 percent of cases are diagnosed in men over age 65. The average age at the time of diagnosis is 65.

---

### 25. [q9263] Stroke
- **Focus Area**: Stroke
- **Data Source**: National Institute of Neurological Disorders and Stroke (NINDS)
- **Question**: What is (are) Stroke ?

**Gold Standard Reference Answer**:
> A stroke occurs when the blood supply to part of the brain is suddenly interrupted or when a blood vessel in the brain bursts, spilling blood into the spaces surrounding brain cells. Brain cells die when they no longer receive oxygen and nutrients from the blood or there is sudden bleeding into or around the brain. The symptoms of a stroke include sudden numbness or weakness, especially on one side of the body; sudden confusion or trouble speaking or understanding speech; sudden trouble seeing in one or both eyes; sudden trouble with walking, dizziness, or loss of balance or coordination; or sudden severe headache with no known cause. There are two forms of stroke: ischemic - blockage of a blood vessel supplying the brain, and hemorrhagic - bleeding into or around the brain.

---

### 26. [q399] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Breast Cancer ?

**Gold Standard Reference Answer**:
> You can seek conventional treatment from a specialized cancer doctor, called an oncologist. The oncologist will usually assemble a team of specialists to guide your therapy. Besides the oncologist, the team may include a surgeon, a radiation oncologist who is a specialist in radiation therapy, and others. Before starting treatment, you may want another doctor to review the diagnosis and treatment plan. Some insurance companies require a second opinion. Others may pay for a second opinion if you request it. You might also be eligible to enroll in a clinical trial to receive treatment that conventional therapies may not offer.

---

### 27. [q520] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Stroke ?

**Gold Standard Reference Answer**:
> The most commonly used imaging procedure is the computed tomography or CT scan, also known as a CAT scan. A CT scan is comprised of a series of cross-sectional images of the head and brain. Because it is readily available at all hours at most major hospitals, produces images quickly, and is good for ruling out hemorrhage prior to starting thrombolytic therapy, CT is the most widely used diagnostic imaging technique for acute stroke. A CT scan may show evidence of early ischemia  an area of tissue that is dead or dying due to a loss of blood supply. Ischemic strokes generally show up on a CT scan about six to eight hours after the start of stroke symptoms.

---

### 28. [q770] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: What is (are) Breast Cancer ?

**Gold Standard Reference Answer**:
> Key Points
                    - Breast cancer is a disease in which malignant (cancer) cells form in the tissues of the breast.    - Sometimes breast cancer occurs in women who are pregnant or have just given birth.     - Signs of breast cancer include a lump or change in the breast.    - It may be difficult to detect (find) breast cancer early in pregnant or nursing women.     - Breast exams should be part of prenatal and postnatal care.    - Tests that examine the breasts are used to detect (find) and diagnose breast cancer.    - If cancer is found, tests are done to study the cancer cells.    - Certain factors affect prognosis (chance of recovery) and treatment options.
                
                
                    Breast cancer is a disease in which malignant (cancer) cells form in the tissues of the breast.
                    The breast is made up of lobes and ducts. Each breast has 15 to 20 sections called lobes. Each lobe has many smaller sections called lobules. Lobules end in dozens of tiny bulbs that can make milk. The lobes, lobules, and bulbs are linked by thin tubes called ducts.      Each breast also has blood vessels and lymph vessels. The lymph vessels carry an almost colorless fluid called lymph. Lymph vessels carry lymph between lymph nodes. Lymph nodes are small bean-shaped structures that are found throughout the body. They filter substances in lymph and help fight infection and disease. Clusters of lymph nodes are found near the breast in the axilla (under the arm), above the collarbone, and in the chest.
                
                
                    It may be difficult to detect (find) breast cancer early in pregnant or nursing women.
                    The breasts usually get larger, tender, or lumpy in women who are pregnant, nursing, or have just given birth. This occurs because of normal hormone changes that take place during pregnancy. These changes can make small lumps difficult to detect. The breasts may also become denser. It is more difficult to detect breast cancer in women with dense breasts using mammography. Because these breast changes can delay diagnosis, breast cancer is often found at a later stage in these women.
                
		        
		            Other Information About Pregnancy and Breast Cancer
		            
		                
		                    Key Points
		                    - Lactation (breast milk production) and breast-feeding should be stopped if surgery or chemotherapy is planned.     - Breast cancer does not appear to harm the unborn baby.    - Pregnancy does not seem to affect the survival of women who have had breast cancer in the past.
		                
		                
		                    Lactation (breast milk production) and breast-feeding should be stopped if surgery or chemotherapy is planned.
		                    If surgery is planned, breast-feeding should be stopped to reduce blood flow in the breasts and make them smaller. Breast-feeding should also be stopped if chemotherapy is planned. Many anticancer drugs, especially cyclophosphamide and methotrexate, may occur in high levels in breast milk and may harm the nursing baby. Women receiving chemotherapy should not breast-feed. Stopping lactation does not improve the mother's prognosis.
		                
		                
		                    Breast cancer does not appear to harm the unborn baby.
		                    Breast cancer cells do not seem to pass from the mother to the unborn baby.
		                
		                
		                    Pregnancy does not seem to affect the survival of women who have had breast cancer in the past.
		                    For women who have had breast cancer, pregnancy does not seem to affect their survival. However, some doctors recommend that a woman wait 2 years after treatment for breast cancer before trying to have a baby, so that any early return of the cancer would be detected. This may affect a womans decision to become pregnant. The unborn baby does not seem to be affected if the mother has had breast cancer.

---

### 29. [q401] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Breast Cancer ?

**Gold Standard Reference Answer**:
> Once breast cancer has been found, it is staged. Staging means determining how far the cancer has progressed. Through staging, the doctor can tell if the cancer has spread and, if so, to what parts of the body. More tests may be performed to help determine the stage. Knowing the stage of the disease helps the doctor plan treatment. Staging will let the doctor know - the size of the tumor and exactly where it is in the breast.  - if the cancer has spread within the breast.  - if cancer is present in the lymph nodes under the arm.  - If cancer is present in other parts of the body. the size of the tumor and exactly where it is in the breast. if the cancer has spread within the breast. if cancer is present in the lymph nodes under the arm. If cancer is present in other parts of the body.  Read more details about the stages of breast cancer.

---

### 30. [q169] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Prostate Cancer ?

**Gold Standard Reference Answer**:
> How Tumors Form The body is made up of many types of cells. Normally, cells grow, divide, and produce more cells as needed to keep the body healthy and functioning properly. Sometimes, however, the process goes wrong -- cells become abnormal and form more cells in an uncontrolled way. These extra cells form a mass of tissue, called a growth or tumor. Tumors can be benign, which means not cancerous, or malignant, which means cancerous. How Prostate Cancer Occurs Prostate cancer occurs when a tumor forms in the tissue of the prostate, a gland in the male reproductive system. In its early stage, prostate cancer needs the male hormone testosterone to grow and survive. The prostate is about the size of a large walnut. It is located below the bladder and in front of the rectum. The prostate's main function is to make fluid for semen, a white substance that carries sperm. Prostate cancer is one of the most common types of cancer among American men. It is a slow-growing disease that mostly affects older men. In fact, more than 60 percent of all prostate cancers are found in men over the age of 65. The disease rarely occurs in men younger than 40 years of age. Prostate Cancer Can Spread Sometimes, cancer cells break away from a malignant tumor in the prostate and enter the bloodstream or the lymphatic system and travel to other organs in the body. When cancer spreads from its original location in the prostate to another part of the body such as the bone, it is called metastatic prostate cancer -- not bone cancer. Doctors sometimes call this distant disease. Surviving Prostate Cancer Today, more men are surviving prostate cancer than ever before. Treatment can be effective, especially when the cancer has not spread beyond the region of the prostate.

---

### 31. [q181] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: Who is at risk for Prostate Cancer? ?

**Gold Standard Reference Answer**:
> Yes. Race is another major risk factor. In the United States, this disease is much more common in African American men than in any other group of men. It is least common in Asian and American Indian men. A man's risk for developing prostate cancer is higher if his father or brother has had the disease. Diet also may play a role. There is some evidence that a diet high in animal fat may increase the risk of prostate cancer and a diet high in fruits and vegetables may decrease the risk. Studies to find out whether men can reduce their risk of prostate cancer by taking certain dietary supplements are ongoing.

---

### 32. [q396] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the symptoms of Breast Cancer ?

**Gold Standard Reference Answer**:
> When breast cancer first develops, there may be no symptoms at all. But as the cancer grows, it can cause changes that women should watch for. You can help safeguard your health by learning the following warning signs of breast cancer. - a lump or thickening in or near the breast or in the underarm area  - a change in the size or shape of the breast  - ridges or pitting of the breast; the skin looks like the skin of an orange  - a change in the way the skin of the breast, areola, or nipple looks or feels; for example, it may be warm, swollen, red, or scaly  - nipple discharge or tenderness, or the nipple is pulled back or inverted into the breast. a lump or thickening in or near the breast or in the underarm area a change in the size or shape of the breast ridges or pitting of the breast; the skin looks like the skin of an orange a change in the way the skin of the breast, areola, or nipple looks or feels; for example, it may be warm, swollen, red, or scaly nipple discharge or tenderness, or the nipple is pulled back or inverted into the breast. You should see your doctor about any symptoms like these. Most often, they are not cancer, but it's important to check with the doctor so that any problems can be diagnosed and treated as early as possible.

---

### 33. [q405] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Breast Cancer ?

**Gold Standard Reference Answer**:
> Radiation therapy uses high-energy x-rays or other types of radiation to kill cancer cells and shrink tumors. This therapy often follows a lumpectomy, and is sometimes used after mastectomy. During radiation therapy, a machine outside the body sends high-energy beams to kill the cancer cells that may still be present in the affected breast or in nearby lymph nodes. Doctors sometimes use radiation therapy along with chemotherapy, or before or instead of surgery.

---

### 34. [q193] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Prostate Cancer ?

**Gold Standard Reference Answer**:
> Regardless of the type of treatment you receive, you will be closely monitored to see how well the treatment is working. Monitoring may include - a PSA blood test, usually every 3 months to 1 year.  - bone scan and/or CT scan to see if the cancer has spread. a PSA blood test, usually every 3 months to 1 year. bone scan and/or CT scan to see if the cancer has spread. - a complete blood count to monitor for signs and symptoms of anemia.  - looking for signs or symptoms that the disease might be progressing, such as fatigue, increased pain, or decreased bowel and bladder function. a complete blood count to monitor for signs and symptoms of anemia. looking for signs or symptoms that the disease might be progressing, such as fatigue, increased pain, or decreased bowel and bladder function.

---

### 35. [q517] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: How to prevent Stroke ?

**Gold Standard Reference Answer**:
> Yes. Stroke is preventable. A better understanding of the causes of stroke has helped people make lifestyle changes that have cut the stroke death rate nearly in half in the last two decades. While family history of stroke plays a role in your risk, there are many risk factors you can control: - If you have high blood pressure, work with your doctor to get it under control.  Managing your high blood pressure is the most important thing you can do to avoid stroke. See ways to manage high blood pressure.     -  If you smoke, quit. See resources to help you quit, including , smoking quitlines,  an online quit plan, a quit smoking website for older adults, and mobile apps and free text messaging services.  If you have high blood pressure, work with your doctor to get it under control.  Managing your high blood pressure is the most important thing you can do to avoid stroke. See ways to manage high blood pressure.     If you smoke, quit. See resources to help you quit, including , smoking quitlines,  an online quit plan, a quit smoking website for older adults, and mobile apps and free text messaging services. - If you have diabetes, learn how to manage it.  Many people do not realize they have diabetes, which is a major risk factor for heart disease and stroke. See ways to manage diabetes every day.     -  If you are overweight, start maintaining a healthy diet and exercising regularly. See a sensible approach to weight loss.  See exercises tailored for older adults.  If you have diabetes, learn how to manage it.  Many people do not realize they have diabetes, which is a major risk factor for heart disease and stroke. See ways to manage diabetes every day.     If you are overweight, start maintaining a healthy diet and exercising regularly. See a sensible approach to weight loss.  See exercises tailored for older adults.  - If you have high cholesterol, work with your doctor to lower it.  A high level of total cholesterol in the blood is a major risk factor for heart disease, which raises your risk of stroke.  Learn about lifestyle changes to control cholesterol.   If you have high cholesterol, work with your doctor to lower it.  A high level of total cholesterol in the blood is a major risk factor for heart disease, which raises your risk of stroke.  Learn about lifestyle changes to control cholesterol.

---

### 36. [q1309] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: Who is at risk for Prostate Cancer? ?

**Gold Standard Reference Answer**:
> Prostate cancer is most common in older men. In the U.S., about one out of five men will be diagnosed with prostate cancer. Most men diagnosed with prostate cancer do not die of it.    See the following PDQ summaries for more information about prostate cancer:         -  Prostate Cancer Screening     -  Prostate Cancer Treatment

---

### 37. [q892] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: How to prevent Breast Cancer ?

**Gold Standard Reference Answer**:
> Key Points
                    - Avoiding risk factors and increasing protective factors may help prevent cancer.    - The following are risk factors for breast cancer:         - Older age     - A personal history of breast cancer or benign (noncancer) breast disease     - Inherited risk of breast cancer     - Dense breasts     - Exposure of breast tissue to estrogen made in the body     - Taking hormone therapy for symptoms of menopause      - Radiation therapy to the breast or chest     - Obesity     - Drinking alcohol         - The following are protective factors for breast cancer:         - Less exposure of breast tissue to estrogen made by the body     - Taking estrogen-only hormone therapy after hysterectomy, selective estrogen receptor modulators, or aromatase inhibitors and inactivators             - Estrogen-only hormone therapy after hysterectomy       - Selective estrogen receptor modulators       - Aromatase inhibitors and inactivators           -  Risk-reducing mastectomy      - Ovarian ablation     - Getting enough exercise        - It is not clear whether the following affect the risk of breast cancer:         - Oral contraceptives     - Environment        - Studies have shown that some factors do not affect the risk of breast cancer.    - Cancer prevention clinical trials are used to study ways to prevent cancer.    - New ways to prevent breast cancer are being studied in clinical trials.
                
                
                    Avoiding risk factors and increasing protective factors may help prevent cancer.
                    Avoiding cancer risk factors may help prevent certain cancers. Risk factors include smoking, being overweight, and not getting enough exercise. Increasing protective factors such as quitting smoking and exercising may also help prevent some cancers. Talk to your doctor or other health care professional about how you might lower your risk of cancer.    NCI's Breast Cancer Risk Assessment Tool uses a woman's risk factors to estimate her risk for breast cancer during the next five years and up to age 90. This online tool is meant to be used by a health care provider. For more information on breast cancer risk, call 1-800-4-CANCER.
                
                
                    The following are risk factors for breast cancer:
                    Older age    Older age is the main risk factor for most cancers. The chance of getting cancer increases as you get older.        A personal history of breast cancer or benign (noncancer) breast disease    Women with any of the following have an increased risk of breast cancer:            - A personal history of invasive breast cancer, ductal carcinoma in situ (DCIS), or lobular carcinoma in situ (LCIS).     - A personal history of benign (noncancer) breast disease.              Inherited risk of breast cancer    Women with a family history of breast cancer in a first-degree relative (mother, sister, or daughter) have an increased risk of breast cancer.    Women who have inherited changes in the  BRCA1  and  BRCA2  genes or in certain other genes have a higher risk of breast cancer. The risk of breast cancer caused by inherited gene changes depends on the type of gene mutation, family history of cancer, and other factors.        Dense breasts    Having breast tissue that is dense on a mammogram is a factor in breast cancer risk. The level of risk depends on how dense the breast tissue is. Women with very dense breasts have a higher risk of breast cancer than women with low breast density.    Increased breast density is often an inherited trait, but it may also occur in women who have not had children, have a first pregnancy late in life, take postmenopausal hormones, or drink alcohol.       Exposure of breast tissue to estrogen made in the body     Estrogen is a hormone made by the body. It helps the body develop and maintain female sex characteristics. Being exposed to estrogen over a long time may increase the risk of breast cancer. Estrogen levels are highest during the years a woman is menstruating.     A woman's exposure to estrogen is increased in the following ways:            -  Early menstruation: Beginning to have menstrual periods at age 11 or younger increases the number of years the breast tissue is exposed to estrogen.     -  Starting menopause at a later age: The more years a woman menstruates, the longer her breast tissue is exposed to estrogen.     -  Older age at first birth or never having given birth: Because estrogen levels are lower during pregnancy, breast tissue is exposed to more estrogen in women who become pregnant for the first time after age 35 or who never become pregnant.              Taking hormone therapy for symptoms of menopause     Hormones, such as estrogen and progesterone, can be made into a pill form in a laboratory. Estrogen, progestin, or both may be given to replace the estrogen no longer made by the ovaries in postmenopausal women or women who have had their ovaries removed. This is called hormone replacement therapy (HRT) or hormone therapy (HT). Combination HRT/HT is estrogen combined with progestin. This type of HRT/HT increases the risk of breast cancer. Studies show that when women stop taking estrogen combined with progestin, the risk of breast cancer decreases.       Radiation therapy to the breast or chest     Radiation therapy to the chest for the treatment of cancer increases the risk of breast cancer, starting 10 years after treatment. The risk of breast cancer depends on the dose of radiation and the age at which it is given. The risk is highest if radiation treatment was used during puberty, when breasts are forming.     Radiation therapy to treat cancer in one breast does not appear to increase the risk of cancer in the other breast.    For women who have inherited changes in the BRCA1 and BRCA2 genes, exposure to radiation, such as that from chest x-rays, may further increase the risk of breast cancer, especially in women who were x-rayed before 20 years of age.       Obesity     Obesity increases the risk of breast cancer, especially in postmenopausal women who have not used hormone replacement therapy.       Drinking alcohol     Drinking alcohol increases the risk of breast cancer. The level of risk rises as the amount of alcohol consumed rises.
                
                
                    The following are protective factors for breast cancer:
                    Less exposure of breast tissue to estrogen made by the body    Decreasing the length of time a woman's breast tissue is exposed to estrogen may help prevent breast cancer. Exposure to estrogen is reduced in the following ways:            -   Early pregnancy: Estrogen levels are lower during pregnancy. Women who have a full-term pregnancy before age 20 have a lower risk of breast cancer than women who have not had children or who give birth to their first child after age 35.     -  Breast-feeding: Estrogen levels may remain lower while a woman is breast-feeding. Women who breastfed have a lower risk of breast cancer than women who have had children but did not breastfeed.              Taking estrogen-only hormone therapy after hysterectomy, selective estrogen receptor modulators, or aromatase inhibitors and inactivators       Estrogen-only hormone therapy after hysterectomy     Hormone therapy with estrogen only may be given to women who have had a hysterectomy. In these women, estrogen-only therapy after menopause may decrease the risk of breast cancer. There is an increased risk of stroke and heart and blood vessel disease in postmenopausal women who take estrogen after a hysterectomy.          Selective estrogen receptor modulators      Tamoxifen and raloxifene belong to the family of drugs called selective estrogen receptor modulators (SERMs). SERMs act like estrogen on some tissues in the body, but block the effect of estrogen on other tissues.     Treatment with tamoxifen lowers the risk of estrogen receptor-positive (ER-positive) breast cancer and ductal carcinoma in situ in premenopausal and postmenopausal women at high risk. Treatment with raloxifene also lowers the risk of breast cancer in postmenopausal women. With either drug, the reduced risk lasts for several years or longer after treatment is stopped. Lower rates of broken bones have been noted in patients taking raloxifene.      Taking tamoxifen increases the risk of hot flashes, endometrial cancer, stroke, cataracts, and blood clots (especially in the lungs and legs). The risk of having these problems increases markedly in women older than 50 years compared with younger women. Women younger than 50 years who have a high risk of breast cancer may benefit the most from taking tamoxifen. The risk of having these problems decreases after tamoxifen is stopped. Talk with your doctor about the risks and benefits of taking this drug.      Taking raloxifene increases the risk of blood clots in the lungs and legs, but does not appear to increase the risk of endometrial cancer. In postmenopausal women with osteoporosis (decreased bone density), raloxifene lowers the risk of breast cancer for women who have a high or low risk of breast cancer. It is not known if raloxifene would have the same effect in women who do not have osteoporosis. Talk with your doctor about the risks and benefits of taking this drug.     Other SERMs are being studied in clinical trials.          Aromatase inhibitors and inactivators      Aromatase inhibitors (anastrozole, letrozole) and inactivators (exemestane) lower the risk of recurrence and of new breast cancers in women who have a history of breast cancer. Aromatase inhibitors also decrease the risk of breast cancer in women with the following conditions:                -  Postmenopausal women with a personal history of breast cancer.      -  Women with no personal history of breast cancer who are 60 years and older, have a history of ductal carcinoma in situ with mastectomy, or have a high risk of breast cancer based on the Gail model tool (a tool used to estimate the risk of breast cancer).               In women with an increased risk of breast cancer, taking aromatase inhibitors decreases the amount of estrogen made by the body. Before menopause, estrogen is made by the ovaries and other tissues in a woman's body, including the brain, fat tissue, and skin. After menopause, the ovaries stop making estrogen, but the other tissues do not. Aromatase inhibitors block the action of an enzyme called aromatase, which is used to make all of the body's estrogen. Aromatase inactivators stop the enzyme from working.     Possible harms from taking aromatase inhibitors include muscle and joint pain, osteoporosis, hot flashes, and feeling very tired.           Risk-reducing mastectomy     Some women who have a high risk of breast cancer may choose to have a risk-reducing mastectomy (the removal of both breasts when there are no signs of cancer). The risk of breast cancer is much lower in these women and most feel less anxious about their risk of breast cancer. However, it is very important to have a cancer risk assessment and counseling about the different ways to prevent breast cancer before making this decision.       Ovarian ablation    The ovaries make most of the estrogen that is made by the body. Treatments that stop or lower the amount of estrogen made by the ovaries include surgery to remove the ovaries, radiation therapy, or taking certain drugs. This is called ovarian ablation.    Premenopausal women who have a high risk of breast cancer due to certain changes in the BRCA1 and BRCA2 genes may choose to have a risk-reducing oophorectomy (the removal of both ovaries when there are no signs of cancer). This decreases the amount of estrogen made by the body and lowers the risk of breast cancer. Risk-reducing oophorectomy also lowers the risk of breast cancer in normal premenopausal women and in women with an increased risk of breast cancer due to radiation to the chest. However, it is very important to have a cancer risk assessment and counseling before making this decision. The sudden drop in estrogen levels may cause the symptoms of menopause to begin. These include hot flashes, trouble sleeping, anxiety, and depression. Long-term effects include decreased sex drive, vaginal dryness, and decreased bone density.        Getting enough exercise    Women who exercise four or more hours a week have a lower risk of breast cancer. The effect of exercise on breast cancer risk may be greatest in premenopausal women who have normal or low body weight.
                
                
                    It is not clear whether the following affect the risk of breast cancer:
                    Oral contraceptives    Certain oral contraceptives contain estrogen. Some studies have shown that taking oral contraceptives ("the pill") may slightly increase the risk of breast cancer in current users. This risk decreases over time. Other studies have not shown an increased risk of breast cancer in women who take oral contraceptives.     Progestin -only contraceptives that are injected or implanted do not appear to increase the risk of breast cancer. More studies are needed to know whether progestin-only oral contraceptives increase the risk of breast cancer.       Environment    Studies have not proven that being exposed to certain substances in the environment, such as chemicals, increases the risk of breast cancer.
                
                
                    Studies have shown that some factors do not affect the risk of breast cancer.
                    The following do not affect the risk of breast cancer:            - Having an abortion.     - Making diet changes such as eating less fat or more fruits and vegetables.     - Taking vitamins, including fenretinide (a type of vitamin A).     -  Cigarette smoking, both active and passive (inhaling secondhand smoke).     -  Using underarm deodorant or antiperspirant.     - Taking statins (cholesterol -lowering drugs).     - Taking bisphosphonates (drugs used to treat osteoporosis and hypercalcemia) by mouth or by intravenous infusion.
                
                
                    Cancer prevention clinical trials are used to study ways to prevent cancer.
                    Cancer prevention clinical trials are used to study ways to lower the risk of developing certain types of cancer. Some cancer prevention trials are conducted with healthy people who have not had cancer but who have an increased risk for cancer. Other prevention trials are conducted with people who have had cancer and are trying to prevent another cancer of the same type or to lower their chance of developing a new type of cancer. Other trials are done with healthy volunteers who are not known to have any risk factors for cancer.   The purpose of some cancer prevention clinical trials is to find out whether actions people take can prevent cancer. These may include exercising more or quitting smoking or taking certain medicines, vitamins, minerals, or food supplements.
                
                
                    New ways to prevent breast cancer are being studied in clinical trials.

---

### 38. [q184] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the symptoms of Prostate Cancer ?

**Gold Standard Reference Answer**:
> Yes. Any of the symptoms caused by prostate cancer may also be due to enlargement of the prostate, which is not cancer. If you have any of the symptoms mentioned in question #10, see your doctor or a urologist to find out if you need treatment. A urologist is a doctor who specializes in treating diseases of the genitourinary system.

---

### 39. [q527] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Stroke ?

**Gold Standard Reference Answer**:
> For more information on stroke, including research sponsored by the National Institute of Neurological Disorders and Stroke, call 1-800-352-9424 or visit the Web site at www.ninds.nih.gov.

---

### 40. [q191] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Prostate Cancer ?

**Gold Standard Reference Answer**:
> Radiation therapy uses high-energy x-rays to kill cancer cells and shrink tumors. Doctors may recommend it instead of surgery or after surgery to destroy any cancer cells that may remain in the area. In advanced stages, the doctor may recommend it to relieve pain or other symptoms. Radiation can cause problems with impotence and bowel function. The radiation may come from a machine, which is external radiation, or from tiny radioactive seeds placed inside or near the tumor, which is internal radiation. Men who receive only the radioactive seeds usually have small tumors. Some men receive both kinds of radiation therapy. For external radiation therapy, patients go to the hospital or clinic -- usually 5 days a week for several weeks. Internal radiation may require patients to stay in the hospital for a short time.

---

### 41. [q398] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: Who is at risk for Breast Cancer? ?

**Gold Standard Reference Answer**:
> The risks of breast cancer screening tests include the following. - Finding breast cancer may not improve health or help a woman live longer. Screening may not help you if you have fast-growing breast cancer or if it has already spread to other places in your body. Also, some breast cancers found on a screening mammogram may never cause symptoms or become life-threatening. Finding these cancers is called overdiagnosis.  Finding breast cancer may not improve health or help a woman live longer. Screening may not help you if you have fast-growing breast cancer or if it has already spread to other places in your body. Also, some breast cancers found on a screening mammogram may never cause symptoms or become life-threatening. Finding these cancers is called overdiagnosis. - False-negative test results can occur. Screening test results may appear to be normal even though breast cancer is present. A woman who receives a false-negative test result (one that shows there is no cancer when there really is) may delay seeking medical care even if she has symptoms. False-negative test results can occur. Screening test results may appear to be normal even though breast cancer is present. A woman who receives a false-negative test result (one that shows there is no cancer when there really is) may delay seeking medical care even if she has symptoms. - False-positive test results can occur. Screening test results may appear to be abnormal even though no cancer is present. A false-positive test result (one that shows there is cancer when there really isnt) is usually followed by more tests (such as biopsy), which also have risks.  False-positive test results can occur. Screening test results may appear to be abnormal even though no cancer is present. A false-positive test result (one that shows there is cancer when there really isnt) is usually followed by more tests (such as biopsy), which also have risks. - Anxiety from additional testing may result from false positive results. In one study, women who had a false-positive screening mammogram followed by more testing reported feeling anxiety 3 months later, even though cancer was not diagnosed. However, several studies show that women who feel anxiety after false-positive test results are more likely to schedule regular breast screening exams in the future. Anxiety from additional testing may result from false positive results. In one study, women who had a false-positive screening mammogram followed by more testing reported feeling anxiety 3 months later, even though cancer was not diagnosed. However, several studies show that women who feel anxiety after false-positive test results are more likely to schedule regular breast screening exams in the future. - Mammograms expose the breast to radiation. Being exposed to radiation is a risk factor for breast cancer. The risk of breast cancer from radiation exposure is higher in women who received radiation before age 30 and at high doses. For women older than 40 years, the benefits of an annual screening mammogram may be greater than the risks from radiation exposure.  Mammograms expose the breast to radiation. Being exposed to radiation is a risk factor for breast cancer. The risk of breast cancer from radiation exposure is higher in women who received radiation before age 30 and at high doses. For women older than 40 years, the benefits of an annual screening mammogram may be greater than the risks from radiation exposure. - There may be pain or discomfort during a mammogram. During a mammogram, the breast is placed between 2 plates that are pressed together. Pressing the breast helps to get a better x-ray of the breast. Some women have pain or discomfort during a mammogram.  There may be pain or discomfort during a mammogram. During a mammogram, the breast is placed between 2 plates that are pressed together. Pressing the breast helps to get a better x-ray of the breast. Some women have pain or discomfort during a mammogram. Some women worry about radiation exposure, but the risk of any harm from a mammogram is actually quite small. The doses of radiation used are very low and considered safe. The exact amount of radiation used during a mammogram will depend on several factors. For instance, breasts that are large or dense will require higher doses to get a clear image. Learn more about the risks of breast cancer screening.

---

### 42. [q515] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: Who is at risk for Stroke? ?

**Gold Standard Reference Answer**:
> A risk factor is a condition or behavior that increases your chances of getting a disease. Having a risk factor for stroke doesn't mean you'll have a stroke. On the other hand, not having a risk factor doesn't mean you'll avoid a stroke. But your risk of stroke grows as the number and severity of risk factors increase. Risk factors for stroke include ones that you cannot control and ones that you can control. Some of the risk factors that you cannot control include - Age.  Although stroke can occur at any age, the risk of stroke doubles for each decade between the ages of 55 and 85.   - Gender. Men have a higher risk for stroke, but more women die from stroke. Men generally do not live as long as women, so men are usually younger when they have their strokes and therefore have a higher rate of survival.   - Race. The risk of stroke is higher among African-American and Hispanic Americans.  - Family History.  Family history of stroke increases your risk. Age.  Although stroke can occur at any age, the risk of stroke doubles for each decade between the ages of 55 and 85. Gender. Men have a higher risk for stroke, but more women die from stroke. Men generally do not live as long as women, so men are usually younger when they have their strokes and therefore have a higher rate of survival. Race. The risk of stroke is higher among African-American and Hispanic Americans. Family History.  Family history of stroke increases your risk. The risk factors for stroke that you CAN control include - high blood pressure  -  cigarette smoking   - diabetes  -  high blood cholesterol   -  heart disease.  high blood pressure cigarette smoking diabetes high blood cholesterol heart disease. Experiencing warning signs and having a history of stroke are also risk factors for stroke.

---

### 43. [q1161] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: National Cancer Institute (Cancer.gov)
- **Question**: What are the symptoms of Breast Cancer ?

**Gold Standard Reference Answer**:
> Signs of breast cancer include a lump or change in the breast. These and other signs may be caused by breast cancer or by other conditions. Check with your doctor if you have any of the following:         - A lump or thickening in or near the breast or in the underarm area.    - A change in the size or shape of the breast.    - A dimple or puckering in the skin of the breast.    - A nipple turned inward into the breast.    - Fluid, other than breast milk, from the nipple, especially if it's bloody.    - Scaly, red, or swollen skin on the breast, nipple, or areola (the dark area of skin around the nipple).    - Dimples in the breast that look like the skin of an orange, called peau dorange.

---

### 44. [q384] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: How to diagnose Breast Cancer ?

**Gold Standard Reference Answer**:
> Most cancers in their early, most treatable stages do not cause any symptoms. That is why it's important to have regular tests to check for cancer long before you might notice anything wrong. Detecting Breast Cancer Through Screening When breast cancer is found early, it is more likely to be treated successfully. Checking for cancer in a person who does not have any symptoms is called screening. Screening tests for breast cancer include, among others, clinical breast exams and mammograms. Recent studies have shown that ultrasound and MRI's may also be useful complementary screening tools, particularly in women with mammograms that are not definitive. During a clinical breast exam, the doctor or other health care professional checks the breasts and underarms for lumps or other changes that could be a sign of breast cancer.  A mammogram is a special x-ray of the breast that often can detect cancers that are too small for a woman or her doctor to feel. (Watch the video to learn more about digital mammography and dense breasts. To enlarge the video, click the brackets in the lower right-hand corner. To reduce the video, press the Escape (Esc) button on your keyboard.) Who Should Have a Mammography? Several studies show that mammography screening has reduced the number of deaths from breast cancer. However, some other studies have not shown a clear benefit from mammography. Scientists are continuing to examine the level of benefit that mammography can produce. The U.S. Preventive Services Task Force (USPSTF) recommends a screening mammography for women 50-74 years every two years.  Learn more about the USPSTF mammography recommendations here. Between 5 and 10 percent of mammogram results are abnormal and require more testing. Most of these follow-up tests confirm that no cancer was present. Worried about the cost of a mammogram? Learn about free and low-cost screenings. (Centers for Disease Control and Prevention) How Biopsies are Performed If needed, the most common follow-up test a doctor will recommend is called a biopsy. This is a procedure where a small amount of fluid or tissue is removed from the breast to make a diagnosis. A doctor might perform fine needle aspiration, a needle or core biopsy, or a surgical biopsy. - With fine needle aspiration, doctors numb the area and use a thin needle to remove fluid and/or cells from a breast lump. If the fluid is clear, it may not need to be checked out by a lab.  - For a needle biopsy, sometimes called a core biopsy, doctors use a needle to remove tissue from an area that looks suspicious on a mammogram but cannot be felt. This tissue goes to a lab where a pathologist examines it to see if any of the cells are cancerous.  - In a surgical biopsy, a surgeon removes a sample of a lump or suspicious area. Sometimes it is necessary to remove the entire lump or suspicious area, plus an area of healthy tissue around the edges. The tissue then goes to a lab where a pathologist examines it under a microscope to check for cancer cells.  With fine needle aspiration, doctors numb the area and use a thin needle to remove fluid and/or cells from a breast lump. If the fluid is clear, it may not need to be checked out by a lab. For a needle biopsy, sometimes called a core biopsy, doctors use a needle to remove tissue from an area that looks suspicious on a mammogram but cannot be felt. This tissue goes to a lab where a pathologist examines it to see if any of the cells are cancerous. In a surgical biopsy, a surgeon removes a sample of a lump or suspicious area. Sometimes it is necessary to remove the entire lump or suspicious area, plus an area of healthy tissue around the edges. The tissue then goes to a lab where a pathologist examines it under a microscope to check for cancer cells. Another type of surgical biopsy that removes less breast tissue is called an image-guided needle breast biopsy, or stereotactic biopsy. Eighty percent of U.S. women who have a surgical breast biopsy do not have cancer. However, women who have breast biopsies are at higher risk of developing breast cancer than women who have never had a breast biopsy. Other Detection Methods Magnetic resonance imaging, or MRI, and ultrasound are two other techniques which, as supplements to standard mammography, might help detect breast cancer with greater accuracy. Genetic Detection The most comprehensive study to date of gene mutations in breast cancer, published in September 2012, confirmed that there are four primary subtypes of breast cancer, each with its own biology. The four groups are called intrinsic subtypes of breast cancer and include HER2-enriched (HER2E), Luminal A (LumA), Luminal B (LumB) and Basal-like. The outlook for survival is different for each of these subtypes of breast cancer. Researchers found that one subtype, Basal-like breast cancer, shares many genetic features with a form of ovarian cancer, and that both may respond similarly to drugs that reduce tumor growth or target DNA repair. The authors hope that discovery of these mutations will be an important step in the effort to improve therapies for breast cancer. For the time being, there are no genetic tests that are commercially available based solely on these findings. Soon, however, knowing extensively which breast cancer gene mutations a woman has should help guide precision treatment.

---

### 45. [q512] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Stroke ?

**Gold Standard Reference Answer**:
> There are two kinds of stroke. The most common kind of stroke is called ischemic stroke. It accounts for approximately 80 percent of all strokes. An ischemic stroke is caused by a blood clot that blocks or plugs a blood vessel in the brain. The other kind of stroke is called hemorrhagic stroke. A hemorrhagic stroke is caused by a blood vessel that breaks and bleeds into the brain.

---

### 46. [q8469] Stroke
- **Focus Area**: Stroke
- **Data Source**: NHLBI
- **Question**: What are the treatments for Stroke ?

**Gold Standard Reference Answer**:
> Treatment for a stroke depends on whether it is ischemic or hemorrhagic. Treatment for a transient ischemic attack (TIA) depends on its cause, how much time has passed since symptoms began, and whether you have other medical conditions.
                
Strokes and TIAs are medical emergencies. If you have stroke symptoms, call 911 right away. Do not drive to the hospital or let someone else drive you. Call an ambulance so that medical personnel can begin lifesaving treatment on the way to the emergency room. During a stroke, every minute counts.
                
Once you receive immediate treatment, your doctor will try to treat your stroke risk factors and prevent complications by recommending heart-healthy lifestyle changes.
                
Treating an Ischemic Stroke or Transient Ischemic Attack
                
An ischemic stroke or TIA occurs if an artery that supplies oxygen-rich blood to the brain becomes blocked. Often, blood clots cause the blockages that lead to ischemic strokes and TIAs. Treatment for an ischemic stroke or TIA may include medicines and medical procedures.
                
Medicines
                
If you have a stroke caused by a blood clot, you may be given a clot-dissolving, or clot-busting, medication called tissue plasminogen activator (tPA). A doctor will inject tPA into a vein in your arm. This type of medication must be given within 4hours of symptom onset. Ideally, it should be given as soon as possible. The sooner treatment begins, the better your chances of recovery. Thus, its important to know the signs and symptoms of a stroke and to call 911 right away for emergency care.
                
If you cant have tPA for medical reasons, your doctor may give you antiplatelet medicine that helps stop platelets from clumping together to form blood clots or anticoagulant medicine (blood thinner) that keeps existing blood clots from getting larger. Two common medicines are aspirin and clopidogrel.
                
Medical Procedures
                
If you have carotid artery disease, your doctor may recommend a carotid endarterectomy or carotid arteryangioplasty. Both procedures open blocked carotid arteries.
                
Researchers are testing other treatments for ischemic stroke, such as intra-arterial thrombolysis and mechanical clot removal in cerebral ischemia (MERCI).
                
In intra-arterial thrombolysis, a long flexible tube called a catheter is put into your groin (upper thigh) and threaded to the tiny arteries of the brain. Your doctor can deliver medicine through this catheter to break up a blood clot in the brain.
                
MERCI is a device that can remove blood clots from an artery. During the procedure, a catheter is threaded through a carotid artery to the affected artery in the brain. The device is then used to pull the blood clot out through the catheter.
                
Treating a Hemorrhagic Stroke
                
A hemorrhagic stroke occurs if an artery in the brain leaks blood or ruptures. The first steps in treating a hemorrhagic stroke are to find the cause of bleeding in the brain and then control it. Unlike ischemic strokes, hemorrhagic strokes arent treated with antiplatelet medicines and blood thinners because these medicines can make bleeding worse.
                
If youre taking antiplatelet medicines or blood thinners and have a hemorrhagic stroke, youll be taken off the medicine. If high blood pressure is the cause of bleeding in the brain, your doctor may prescribe medicines to lower your blood pressure. This can help prevent further bleeding.
                
Surgery also may be needed to treat a hemorrhagic stroke. The types of surgery used include aneurysm clipping, coil embolization, and arteriovenous malformation (AVM) repair.
                
Aneurysm Clipping and Coil Embolization
                
If an aneurysm (a balloon-like bulge in an artery) is the cause of a stroke, your doctor may recommend aneurysm clipping or coil embolization.
                
Aneurysm clipping is done to block off the aneurysm from the blood vessels in the brain. This surgery helps prevent further leaking of blood from the aneurysm. It also can help prevent the aneurysm from bursting again.During the procedure, a surgeon will make an incision (cut) in the brain and place a tiny clamp at the base of the aneurysm. Youll be given medicine to make you sleep during the surgery. After the surgery, youll need to stay in the hospitals intensive care unit for a few days.
                
Coil embolization is a less complex procedure for treating an aneurysm. The surgeon will insert a tube called a catheter into an artery in the groin. He or she will thread the tube to the site of the aneurysm.Then, a tiny coil will be pushed through the tube and into the aneurysm. The coil will cause a blood clot to form, which will block blood flow through the aneurysm and prevent it from burstingagain.Coil embolization is done in a hospital. Youll be given medicine to make you sleep during thesurgery.
                
Arteriovenous Malformation Repair
                
If an AVM is the cause of a stroke, your doctor may recommend an AVM repair. (An AVM is a tangle of faulty arteries and veins that can rupture within the brain.) AVM repair helps prevent further bleeding in the brain.
                
Doctors use several methods to repair AVMs. These methods include:
                
Injecting a substance into the blood vessels of the AVM to block blood flow
                
Surgery to remove the AVM
                
Using radiation to shrink the blood vessels of the AVM
                
Treating Stroke Risk Factors
                
After initial treatment for a stroke or TIA, your doctor will treat your risk factors. He or she may recommend heart-healthy lifestyle changes to help control your risk factors.
                
Heart-healthy lifestyle changes may include:
                
heart-healthy eating
                
maintaining a healthy weight
                
managing stress
                
physical activity
                
quitting smoking
                
If lifestyle changes arent enough, you may need medicine to control your risk factors.
                
Heart-Healthy Eating
                
Your doctor may recommend heart-healthy eating, which should include:
                
Fat-free or low-fat dairy products, such as skim milk
                
Fish high in omega-3 fatty acids, such as salmon, tuna, and trout, about twice a week
                
Fruits, such as apples, bananas, oranges, pears, and prunes
                
Legumes, such as kidney beans, lentils, chickpeas, black-eyed peas, and lima beans
                
Vegetables, such as broccoli, cabbage, and carrots
                
Whole grains, such as oatmeal, brown rice, and corn tortillas
                
When following a heart-healthy diet, you should avoid eating:
                
A lot of red meat
                
Palm and coconut oils
                
Sugary foods and beverages
                
Two nutrients in your diet make blood cholesterol levels rise:
                
Saturated fatfound mostly in foods that come from animals
                
Trans fat (trans fatty acids)found in foods made with hydrogenated oils and fats, such as stick margarine; baked goods, such as cookies, cakes, and pies; crackers; frostings; and coffee creamers. Some trans fats also occur naturally in animal fats and meats.
                
Saturated fat raises your blood cholesterol more than anything else in your diet. When you follow a heart-healthy eating plan, only 5percent to 6percent of your daily calories should come from saturated fat. Food labels list the amounts of saturated fat. To help you stay on track, here are some examples:
                
1,200 calories a day
                
8 grams of saturated fat a day
                
1,500 calories a day
                
10 grams of saturated fat a day
                
1,800 calories a day
                
12 grams of saturated fat a day
                
2,000 calories a day
                
13 grams of saturated fat a day
                
2,500 calories a day
                
17 grams of saturated fat a day
                
Not all fats are bad. Monounsaturated and polyunsaturated fats actually help lower blood cholesterol levels. Some sources of monounsaturated and polyunsaturated fats are:
                
Avocados
                
Corn, sunflower, and soybean oils
                
Nuts and seeds, such as walnuts
                
Olive, canola, peanut, safflower, and sesame oils
                
Peanut butter
                
Salmon and trout
                
Tofu
                
Sodium
                
Try to limit the amount of sodium that you eat. This means choosing and preparing foods that are lower in salt and sodium. Try to use low-sodium and no added salt foods and seasonings at the table or while cooking. Food labels tell you what you need to know about choosing foods that are lower in sodium. Try to eat no more than 2,300 milligrams of sodium a day. If you have high blood pressure, you may need to restrict your sodium intake even more.
                
Dietary Approaches to Stop Hypertension
                
Your doctor may recommend the Dietary Approaches to Stop Hypertension (DASH) eating plan if you have high blood pressure. The DASH eating plan focuses on fruits, vegetables, whole grains, and other foods that are heart healthy and low in fat, cholesterol, and sodium and salt.
                
The DASH eating plan is a good heart-healthy eating plan, even for those who dont have high blood pressure. Read more about DASH.
                
Alcohol
                
Try to limit alcohol intake. Too much alcohol can raise your blood pressure and triglyceride levels, a type of fat found in the blood. Alcohol also adds extra calories, which may cause weight gain.
                
Men should have no more than two drinks containing alcohol a day. Women should have no more than one drink containing alcohol a day. One drink is:
                
12 ounces of beer
                
5 ounces of wine
                
1 ounces of liquor
                
Maintaining a Healthy Weight
                
Maintaining a healthy weight is important for overall health and can lower your risk for stroke. Aim for a Healthy Weight by following a heart-healthy eating plan and keeping physically active.
                
Knowing your body mass index (BMI) helps you find out if youre a healthy weight in relation to your height and gives an estimate of your total body fat. To figure out your BMI, check out the National Heart, Lung, and Blood Institutes (NHLBI) online BMI calculator or talk to your doctor. A BMI:
                
Below 18.5 is a sign that you are underweight.
                
Between 18.5 and 24.9 is in the normal range.
                
Between 25.0 and 29.9 is considered overweight.
                
Of 30.0 or higher is considered obese.
                
A general goal to aim for is a BMI of less than 25. Your doctor or health care provider can help you set an appropriate BMI goal.
                
Measuring waist circumference helps screen for possible health risks. If most of your fat is around your waist rather than at your hips, youre at a higher risk for heart disease and type2 diabetes. This risk may be high with a waist size that is greater than 35 inches for women or greater than 40 inches for men. To learn how to measure your waist, visit Assessing Your Weight and Health Risk.
                
If youre overweight or obese, try to lose weight. A loss of just 3 percent to 5 percent of your current weight can lower your triglycerides, blood glucose, and the risk of developing type 2 diabetes. Greater amounts of weight loss can improve blood pressure readings, lower LDL cholesterol, and increase HDL cholesterol.
                
Managing Stress
                
Learning how to manage stress, relax, and cope with problems can improve your emotional and physical health. Consider healthy stress-reducing activities, such as:
                
A stress management program
                
Meditation
                
Physical activity
                
Relaxation therapy
                
Talking things out with friends or family
                
Physical Activity
                
Regular physical activity can lower many risk factors for stroke.
                
Everyone should try to participate in moderate-intensity aerobic exercise at least 2hours and 30minutes per week or vigorous aerobic exercise for 1hour and 15minutes per week. Aerobic exercise, such as brisk walking, is any exercise in which your heart beats faster and you use more oxygen than usual. The more active you are, the more you will benefit. Participate in aerobic exercise for at least 10minutes at a time spread throughout the week.
                
Talk with your doctor before you start a new exercise plan. Ask your doctor how much and what kinds of physical activity are safe for you.
                
Read more about physical activity at:
                
Physical Activity and Your Heart
                
U.S. Department of Health and Human Services, 2008 Physical Activity Guidelines for Americans
                
Quitting Smoking
                
If you smoke or use tobacco, quit. Smoking can damage and tighten blood vessels and raise your risk for stroke. Talk with your doctor about programs and products that can help you quit. Also, try to avoid secondhand smoke. If you have trouble quitting smoking on your own, consider joining a support group. Many hospitals, workplaces, and community groups offer classes to help people quit smoking.
                
For more information about how to quit smoking, visit Smoking and Your Heart.

---

### 47. [q178] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Prostate Cancer ?

**Gold Standard Reference Answer**:
> Sometimes, cancer cells break away from the malignant tumor in the prostate and enter the bloodstream or the lymphatic system and travel to other organs in the body. When cancer spreads from its original location in the prostate to another part of the body such as the bone, it is called metastatic prostate cancer, not bone cancer. Doctors sometimes call this "distant" disease.

---

### 48. [q387] Breast Cancer
- **Focus Area**: Breast Cancer
- **Data Source**: NIH Senior Health
- **Question**: what research (or clinical trials) is being done for Breast Cancer ?

**Gold Standard Reference Answer**:
> New Technologies Several new technologies offer hope for making future treatment easier for women with breast cancer. - Using a special tool, doctors can today insert a miniature camera through the nipple and into a milk duct in the breast to examine the area for cancer.  Using a special tool, doctors can today insert a miniature camera through the nipple and into a milk duct in the breast to examine the area for cancer. - Researchers are testing another technique to help women who have undergone weeks of conventional radiation therapy. Using a small catheter -- a tube with a balloon tip -- doctors can deliver tiny radioactive beads to a place on the breast where cancer tissue has been removed. This can reduce the therapy time to a matter of days. Researchers are testing another technique to help women who have undergone weeks of conventional radiation therapy. Using a small catheter -- a tube with a balloon tip -- doctors can deliver tiny radioactive beads to a place on the breast where cancer tissue has been removed. This can reduce the therapy time to a matter of days. New Drug Combination Therapies New drug therapies and combination therapies continue to evolve. - A mix of drugs may increase the length of time you will live or the length of time you will live without cancer. It may someday prove useful for some women with localized breast cancer after they have had surgery.  A mix of drugs may increase the length of time you will live or the length of time you will live without cancer. It may someday prove useful for some women with localized breast cancer after they have had surgery. - New research shows women with early-stage breast cancer who took the drug letrozole, an aromatase inhibitor, after they completed five years of tamoxifen therapy significantly reduced their risk of breast cancer recurrence. New research shows women with early-stage breast cancer who took the drug letrozole, an aromatase inhibitor, after they completed five years of tamoxifen therapy significantly reduced their risk of breast cancer recurrence. Treating HER2-Positive Breast Cancer Herceptin is a drug commonly used to treat women who have a certain type of breast cancer. This drug slows or stops the growth of cancer cells by blocking HER2, a protein found on the surface of some types of breast cancer cells. Approximately 20 to 25 percent of breast cancers produce too much HER2. These "HER2 positive" tumors tend to grow faster and are generally more likely to return than tumors that do not overproduce HER2. Results from clinical trials show that those patients with early-stage HER2 positive breast cancer who received Herceptin in combination with chemotherapy had a 52 percent decrease in risk in the cancer returning compared with patients who received chemotherapy treatment alone. Cancer treatments like chemotherapy can be systemic, meaning they affect whole tissues, organs, or the entire body. Herceptin, however, was the first drug used to target only a specific molecule involved in breast cancer. Another drug, Tykerb, was approved by the U.S. Food and Drug Administration for use for treatment of HER2-positive breast cancer. Because of the availability of these two drugs, an international trial called ALTTO was designed to determine if one drug is more effective, safer, and if taking the drugs separately, in tandem order, or together is better. Unfortunately, the results, released in 2014, showed that taking two HER2-targeted agents together was no better than taking one alone in improving survival. The TAILORx Trial In an attempt to further specialize breast cancer treatment, The Trial Assigning Individualized Options for Treatment, or TAILORx, enrolled 10,000 women to examine whether appropriate treatment can be assigned based on genes that are frequently associated with risk of recurrence of breast cancer. The goal of TAILORx is important because the majority of women with early-stage breast cancer are advised to receive chemotherapy in addition to radiation and hormonal therapy, yet research has not demonstrated that chemotherapy benefits all of them equally. TAILORx seeks to examine many of a woman's genes simultaneously and use this information in choosing a treatment course, thus sparing women unnecessary treatment if chemotherapy is not likely to be of substantial benefit to them.

---

### 49. [q516] Stroke
- **Focus Area**: Stroke
- **Data Source**: NIH Senior Health
- **Question**: What is (are) Stroke ?

**Gold Standard Reference Answer**:
> Atherosclerosis, also known as hardening of the arteries, is the most common blood vessel disease. It is caused by the buildup of fatty deposits in the arteries, and is a risk factor for stroke.

---

### 50. [q194] Prostate Cancer
- **Focus Area**: Prostate Cancer
- **Data Source**: NIH Senior Health
- **Question**: What are the treatments for Prostate Cancer ?

**Gold Standard Reference Answer**:
> Through research, doctors are trying to find new, more effective ways to treat prostate cancer. Cryosurgery -- destroying cancer by freezing it -- is under study as an alternative to surgery and radiation therapy. To avoid damaging healthy tissue, the doctor places an instrument known as a cryoprobe in direct contact with the tumor to freeze it. Doctors are studying new ways of using radiation therapy and hormonal therapy, too. Studies have shown that hormonal therapy given after radiation therapy can help certain men whose cancer has spread to nearby tissues. Scientists are also testing the effectiveness of chemotherapy and biological therapy for men whose cancer does not respond or stops responding to hormonal therapy. They are also exploring new ways to schedule and combine various treatments. For example, they are studying hormonal therapy to find out if using it to shrink the tumor before a man has surgery or radiation might be a useful approach. They are also testing combinations of hormone therapy and vaccines to prevent recurrence of prostate cancer. In 2010, the FDA approved a therapeutic cancer vaccine, Provenge, for use in some men with metastatic prostate cancer. This approval was based on the results of a clinical trial that demonstrated a more than 4-month improvement in overall survival compared with a placebo vaccine. Other similar vaccine therapies are in development.

---


# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
 Args:
        number (int, optional): Загаданное число. Defaults to 1.

Returns:
        int: Число попыток
  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  
import { execFile } from 'child_process';
import { mkdirSync, writeFileSync } from 'fs';
import { join } from 'path';
import type {
  Application,
  AppBuildContext,
  AppBuildResult,
} from '@teambit/application';
import type { MyAppTypeOptions } from './my-app-type.app-type';

export class MyApp implements Application {
  /** properties set by the app (component) using this app-type */
  constructor(
    readonly name: MyAppTypeOptions['name'],
    readonly entry: MyAppTypeOptions['entry'],
    /**
     * this app type does not implement its own deployment.
     * to learn more see: https://bit.dev/docs/apps/app-deployment
     *  */
    readonly deploy?: MyAppTypeOptions['deploy']
  ) {}

  async run(): Promise<void> {
    const child = execFile('node', [this.entry], (error) => {
      if (error) {
        throw error;
      }
    });
  }

  async build(context: AppBuildContext): Promise<AppBuildResult> {
    const appCapsulePath = context.capsule.path;
    const appArtifactsDir = join(appCapsulePath, 'artifacts-to-be-deployed');
    mkdirSync(appArtifactsDir);
    writeFileSync(join(appArtifactsDir, 'dummy-artifact.js'), '');
    return {
      artifacts: [
        {
          name: 'my-build-artifacts',
          /**
           * the glob pattern to select this app's generated artifacts.
           * these will be available for the app's deploy function.
           * */
          globPatterns: ['artifacts-to-be-deployed/**'],
        },
      ],
    };
  }
}

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
Алгоритм угадывает число в среднем за 4 попытки.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
Для наилучших результатов необходимо использовать двоичный (или бинарный) поиск элемента.

:arrow_up:[к оглавлению](.README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common'; // Import CommonModule
import { ServiceService } from './service.service';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';
import { MyTestComponent } from '../my-test/my-test.component';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [ReactiveFormsModule,CommonModule,MyTestComponent]
  
})
export class AppComponent implements OnInit {
  newdata: any;
  newdata2: any;
  search_var: any;
  imagePaths: SafeUrl[] = [];
  selectedNode: any;
  selectedImagePath: any;

  myForm: FormGroup;



  constructor(private fb: FormBuilder,private _apiservice: ServiceService, private _domSanitizer: DomSanitizer) { 
    this.myForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]]
    });
  }

  ngOnInit() {
    this.getData();
    this.getTree();
  }


  handleEvent(event: string) {
    alert(event);
  }  
  getData() {
    console.log("startData!");

    this._apiservice.get_data().subscribe((res: any) => {
      this.newdata = res;
      console.log(res);
    });
  }

  getTree() {
    console.log("startTree!");

    this._apiservice.get_tree().subscribe((res: any) => {
      this.newdata2 = res;
      console.log(res);
    });
  }

  open(imgPath: any) {
    this.selectedImagePath = imgPath;
  console.log(this.newdata2.children[0]);
  
    const specificChild = this.newdata2.children.find((child: { Image: any; entity_types: any }) => child.Image === imgPath);
    if (specificChild) {
      if (specificChild.entity_types) {
        console.log("Entities Types for the specific child (maffin):", specificChild.entity_types);
      } else {
        console.log("The specific child does not have entities_types property.");
      }
    } else {
      console.log("Specific child not found in newdata2.children.");
    }
  }
  
  close() {
    this.selectedImagePath = null;
  }

  toggleNode(node: any) {    
    node.expanded = !node.expanded;
    this.selectedNode = node;

    this.imagePaths = [];
    if (node.type === 'folder') {
      this.displayFolderContents(node);
    } else if (node.type === 'file') {
      this.openImage(node);
    }
  }


  displayFolderContents(folderNode: any) {
    console.log("folder!");

    if (Array.isArray(folderNode.children)) {
      for (const item of folderNode.children) {
        if (item.type === 'file') {
          this.openImage(item);
        } 
        else if (item.type === 'folder') {
          this.displayFolderContents(item);
        }
      }
    } else {
      console.log("Children of folderNode are not iterable.");
    }
  }


  openImage(node: { type: string, name: string, imageData: string, image: string }) {
    if (node.type === 'file') {
      console.log('Opening image: ', node.name);
      const safeUrl = this._domSanitizer.bypassSecurityTrustUrl(node.image);
  
      // Check if the image is already in the array before adding it
      if (!this.imagePaths.includes(safeUrl)) {
        this.imagePaths.push(safeUrl); // Add the new image to display it
      }
    } else if (node.type === 'folder') {
      console.log('Opening folder: ', node.name);
      
      // Create a safe URL for the folder image
      const safeUrl = this._domSanitizer.bypassSecurityTrustUrl(node.image);
  
      // Check if the image is already in the array before adding it
      if (!this.imagePaths.includes(safeUrl)) {
        this.imagePaths.push(safeUrl); // Add the folder image to display it
      }
    }
  }
  
  submitForm(): void {
    if (this.myForm.valid) {
      // Form is valid, submit data or perform further actions
      alert('Form submitted:'+ this.myForm.value);
    } else {
      // Form is invalid, handle validation errors
      alert('Form is invalid. Please check the fields.');
    }
  }

  
  
  
  
  
  

  }